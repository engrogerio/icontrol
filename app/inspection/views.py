# -*- coding: utf-8 -*-
import datetime
from app.inspection.forms import InspectionForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from app.inspection.models import Inspection, InspectionTable
from app.tag.models import Tag
from app.value.models import Value
from app.iform.models import IForm, IFormTag
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from app.value.models import Value
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django_tables2 import RequestConfig
from django_tables2 import LazyPaginator


class InspectionList(LoginRequiredMixin, ListView):
    model = Inspection
    context_name = 'inspection'
    ordering = ['iform__name', 'created_when']
    queryset = Inspection.objects.all()
    table = InspectionTable(queryset)
    paginator_class = LazyPaginator

        
    def get_context_data(self, **kwargs):
        context = super(InspectionList, self).get_context_data(**kwargs)
        table = InspectionTable(Inspection.objects.order_by('-pk'))
        # TODO check if this is correct: table.paginate(page=self.request.GET.get("page", 1), per_page=25)
        table.paginator = True
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        context['iform'] = 'iForm'
        return context
    
class InspectionDelete(LoginRequiredMixin, DeleteView):
    model = Inspection
    template_name = 'inspection/inspection_delete.html'
    success_url = reverse_lazy('inspection:inspection_list')


# TODO:Send this to the value model
def add_data(tag, value, data, inspection):
    """
    Gets the data and save it to the correct db value field.
    Rules are:
    BOOL:
        number = 1 OR 0
        text = ''
    TEXT:
        number = None
        text = TEXT

    DATE, TIME & DATETIME:
        # TODO: maybe would be good if save the date INTEGER as Unix Time:
        # the number of seconds since 1970-01-01 00:00:00 UTC.
        number = None
        text = DATETIME

    INTEGER & FLOAT:
        number = INTEGER/FLOAT
        text = None

    CHOICE: TODO
    """

    number = None
    text = None

    if tag.type == tag.BOOL:
        text = str(data)
    elif tag.type in (tag.TEXT, tag.LARGE_TEXT, tag.DATETIME, tag.TIME, 
                      tag.DATE, tag.URL):
        text = str(data)
    elif tag.type == tag.FLOAT:
        number = float(data) if data else None
    elif tag.type == tag.INTEGER:
        number = int(data) if data else None
    elif tag.type in (tag.CHOICES, tag.RADIO):
        text = str(data)
    elif tag.type == tag.CHECKBOX:
        text = ', '.join(data)
    else:
        number = None
        text = str(data)
        
    # finally save the instance in db
    value.tag = tag
    value.inspection = inspection
    value.text = text
    value.number = number
    value.save()

def get_data(tag, inspection):
    data = None
    
    if tag.type in (tag.TEXT, tag.LARGE_TEXT, tag.DATETIME, tag.TIME, tag.DATE,
                    tag.BOOL, tag.CHOICES, tag.RADIO, tag.CHECKBOX, tag.URL):
        try:
            data = Value.objects.filter(inspection=inspection).get(tag=tag).text
        except:
            data = None

    if tag.type == tag.FLOAT:
        try:
            data = round(Value.objects.filter(inspection=inspection).get(tag=tag).number,tag.decimal_places)
        except:
            data = None

    if tag.type == tag.INTEGER:
        try:
            data = int(Value.objects.filter(inspection=inspection).get(tag=tag).number)
        except:
            data = None

    return data

@login_required
def inspection_update (request, pk=None):
    # get the inspection being updated
    inspection = Inspection.objects.get(id=pk)

    # get iform for the inspection being updated
    iform = inspection.iform

    if request.method == 'POST':

        form = InspectionForm(request.POST, iform_id=iform.id)
        if form.is_valid():
            for field in form:
                # TODO: section type tag should not being persisted on the database
                
                tag = Tag.objects.get(id=field.name)
                # try to recover data from Value instance, but if can't, that is due to the tag was created
                # after this inspection had been created. So, it creates a new Value instance.
                try:
                    value = Value.objects.filter(inspection=inspection).get(tag=tag)
                    value.updated_by = request.user
                except Exception as ex:
                    value = Value()
                value.updated_by = request.user
                inspection.updated_by = request.user
                inspection.save()
                data = field.value()
                add_data(tag, value, data, inspection)

            return HttpResponseRedirect(reverse('iform:iform_list'))

    if request.method == 'GET':
        # iterate iform fields and get types / values
        form = InspectionForm(iform_id=iform.id) #request.GET,

        # get the values saved for each field for this specific inspection and tag
        for field in form:
            tag = Tag.objects.get(id=field.name)
            data = get_data(tag, inspection)
            if tag.type == tag.BOOL:
                if data == 'True':
                    field.initial=True
                else:
                    field.initial=False
                    
            elif tag.type == tag.CHECKBOX:
                field.initial = list(data)

            else:
                field.initial = data
    else:
        print(request.method)

    return render(request, 'inspection/inspection_update.html', {'form': form, 'iform': iform})

@login_required
def inspection_create (request, pk=None):
    # get iform for the new inspection
    iform = IForm.objects.get(id=pk)

    if request.method == 'POST':
        form = InspectionForm(request.POST, iform_id=pk)
        if form.is_valid():
            # creates a new inspection based on the iform
            inspection = Inspection()
            inspection.iform = iform
            inspection.created_by = request.user
            inspection.save()

            # creates new Values for each field and...
            for field in form:
                value = Value()
                data = field.value()
                tag = Tag.objects.get(id=field.name)
                value.created_by = request.user
                value.number = tag
                value.inspection = inspection

                # ...finally save the object in db
                add_data(tag, value, data, inspection)
            messages.add_message(request, messages.SUCCESS, 'Inspection was succefully created!')
            return HttpResponseRedirect(reverse('iform:iform_list'))
    if request.method == 'GET':
        # passing the iform id to form so the form knows which fields to show
        form = InspectionForm(iform_id=pk)  # raise Http404
    else:
        print(request.method)

    return render(request, 'inspection/inspection_create.html', {'form': form, 'iform': iform})

# this will work on js-grid
def get_data_collections (request, iform_pk=None):
    """
    Return a list of JSON for the requested iform
    with all (lazy?) data for use in grids or charsd
    """
    # grab all inspections from the requested iform
    inspections = Inspection.objects.filter(iform__id=iform_pk)
    dic = value_dic = {}
    values_list = []
    for inspection in inspections:
        # grab all values for this inspection
        values = Value.objects.filter(inspection_id=inspection.id)
        for value in values:
            tag = Tag.objects.get(id=value.tag_id)
            farg = "{0:."+ str(tag.decimal_places) +"f}"
            #value_dic [tag.name] = value.number if value.number else value.text
            value_dic [tag.name] = str(farg.format(value.number)) if value.number else value.text
        values_list.append(value_dic)
        value_dic={}

    # get list of dictionaries for defining jsGrid fields    
    tags = IFormTag.objects.filter(iform_id=iform_pk).only('tag')
    jsonizable_tag_list = []
    for tag in tags: 
        jsonizable_tag_list.append({"name":tag.tag.name,
        "title":tag.tag.name+' ('+tag.tag.unit+')' if tag.tag.unit else tag.tag.name , "type": tag.tag.jsgrid_type(), "width":tag.tag.max_length})
    #jsonizable_tag_list.append({ "type": "control" })
    return render(request, 'inspection/inspection_values.html',
        {
            "iform": IForm.objects.get(id=iform_pk),
            "value_list": json.dumps(values_list), 
            "tag_list": json.dumps(jsonizable_tag_list)
        })
