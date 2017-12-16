# -*- coding: utf-8 -*-

from app.inspection.forms import InspectionForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from app.inspection.models import Inspection
from app.tag.models import Tag
from app.iform.models import IForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from app.value.models import Value
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class InspectionList(LoginRequiredMixin, ListView):
    model = Inspection
    template_name = 'inspection/inspection_list.html'
    paginate_by = 20


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
        number = ''
        text = TEXT

    DATE, TIME & DATETIME:
        # TODO: maybe would be good if save the date INTEGER as Unix Time:
        # the number of seconds since 1970-01-01 00:00:00 UTC.
        number = ''
        text = DATETIME

    INTEGER & FLOAT:
        number = INTEGER/FLOAT
        text = ''

    CHOICE: TODO
    """

    number = None
    text = None

    if tag.type == tag.BOOL:
        text = str(data)
    elif tag.type in (tag.TEXT, tag.DATETIME, tag.TIME, tag.DATE):
        text = data.encode('utf-8')
    elif tag.type == tag.FLOAT:
        number = float(data) if data else None
    elif tag.type == tag.INTEGER:
        number = int(data) if data else None
    elif tag.type == tag.CHOICES:
        text = str(data)
    else:
        number = int(data) if data else None
        text = str(data)
    # finally save the instance in db

    value.tag = tag
    value.inspection = inspection
    value.text = text
    value.number = number
    value.save()

def get_data(tag, inspection):
    data = None
    
    if tag.type in (tag.TEXT, tag.DATETIME, tag.TIME, tag.DATE, tag.BOOL, tag.CHOICES):
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
                tag = Tag.objects.get(id=field.name)
                # try to recover data from Value instance, but if can't, that is due to the tag was created
                # after this inspection had been created. So, its created a new Value instance.
                try:
                    value = Value.objects.filter(inspection=inspection).get(tag=tag)
                except:
                    value = Value()

                data = field.value()
                add_data(tag, value, data, inspection)

            return HttpResponseRedirect('/inspection/list')

    if request.method == 'GET':
        # iterate iform fields and get types / values
        form = InspectionForm( iform_id=iform.id) #request.GET,

        # get the values saved for each field for this specific inspection and tag
        for field in form:
            tag = Tag.objects.get(id=field.name)
            data = get_data(tag, inspection)
            if tag.type == tag.BOOL:
                if data == 'True':
                    field.initial=True
                else:
                    field.initial=False
            else:
                field.initial = data
    else:
        print(request.method)

    return render(request, 'inspection/inspection_update.html', {'form': form, 'iform': iform.name})

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

            # creates new Values for each field and save to the database
            for field in form:
                value = Value()
                data = field.value()
                tag = Tag.objects.get(id=field.name)
                value.number = tag
                value.inspection = inspection

                # finally save the object in db
                add_data(tag, value, data, inspection)
            messages.add_message(request, messages.SUCCESS, 'Inspection was succefully created!')
            return HttpResponseRedirect('/iform/list')
    if request.method == 'GET':
        # passing the iform id to form so the form knows which fields to show
        form = InspectionForm(iform_id=pk)  # raise Http404
    else:
        print(request.method)

    return render(request, 'inspection/inspection_create.html', {'form': form, 'iform': iform.name})

# from django.views.generic import TemplateView
# from django.contrib.auth.models import User

# import arrow


# class AnalyticsIndexView(TemplateView):
#     template_name = 'analytics/admin/index.html'

#     def get_context_data(self, **kwargs):
#         context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
#         context['30_day_registrations'] = self.thirty_day_registrations()
#         return context

#     def thirty_day_registrations(self):
#         final_data = []

#         date = arrow.now()
#         for day in xrange(1, 30):
#             date = date.replace(days=-1)
#             count = User.objects.filter(
#                 date_joined__gte=date.floor('day').datetime,
#                 date_joined__lte=date.ceil('day').datetime).count()
#             final_data.append(count)

#         return final_data
