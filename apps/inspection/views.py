from apps.inspection.forms import InspectionForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from apps.inspection.models import Inspection
from apps.tag.models import Tag
from apps.iform.models import IForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.value.models import Value


class InspectionList(ListView):
    model = Inspection
    template_name = 'inspection/inspection_list.html'
    paginate_by = 6


class InspectionDelete(DeleteView):
    model = Inspection
    template_name = 'inspection/inspection_delete.html'
    success_url = reverse_lazy('inspection:inspection_list')



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
                # recover the Value object
                obj = Value.objects.filter(inspection=inspection).get(tag=tag)
                # update value value
                # TODO: check on the tag if the value is on Text field or Numeric field of Value
                obj.text = field.value()
                # finally save the object in db
                obj.save()
            return HttpResponseRedirect('/inspection/list')

    if request.method == 'GET':
        # iterate iform fields and get types / values
        form = InspectionForm( iform_id=iform.id) #request.GET,

        # get the values saved for each field for this specific inspection and tag
        for field in form:
            tag = Tag.objects.get(id=field.name)
            value = Value.objects.filter(inspection=inspection).filter(tag=tag).values('text')[0]
            # TODO: check on the tag if the value is on Text field or Numeric field of Value
            field.initial = value['text']
    else:
        print(request.method)

    return render(request, 'inspection/inspection_update.html', {'form': form, 'iform': iform.name})

def inspection_create (request, pk=None):
    # get iform for the new inspection
    iform = IForm.objects.get(id=pk)

    if request.method == 'POST':
        form = InspectionForm(request.POST, iform_id=pk) # , iform_id=pk)
        if form.is_valid():

            # creates a new inspection based on the iform
            inspection = Inspection()
            inspection.iform = iform
            inspection.save()

            # creates new Values for each field
            for field in form:
                obj = Value()
                obj.text = field.value()
                obj.tag = Tag.objects.get(id=field.name)
                obj.inspection = inspection
                # finally save the object in db
                obj.save()
            return HttpResponseRedirect('/iform/list')

    if request.method == 'GET':
        # passing the iform id to form so the form knows which fields to show
        form = InspectionForm(iform_id=pk)# raise Http404
    else:
        print(request.method)

    return render(request, 'inspection/inspection_create.html', {'form': form, 'iform': iform.name})
