from apps.inspection.forms import InspectionForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.http import Http404
from apps.inspection.models import Inspection
from apps.tag.models import Tag
from apps.iform.models import IForm

def TagIndex(request):
    return HttpResponse ('Inspection list')


class InspectionList(ListView):
    model = Inspection
    template_name = 'inspection/inspection_list.html'
    paginate_by = 6


class InspectionCreate(FormView):
    model = Inspection
    template_name = 'inspection/inspection_form.html'
    form_class = InspectionForm
    success_url = reverse_lazy('inspection:inspection_list')


class InspectionUpdate(UpdateView):
    model = Inspection
    template_name = 'inspection/inspection_update.html'
    form_class = InspectionForm
    success_url = reverse_lazy('inspection:inspection_list')


class InspectionDelete(DeleteView):
    model = Inspection
    template_name = 'inspection/inspection_delete.html'
    #form_class = TagForm
    success_url = reverse_lazy('inspection:inspection_list')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.value.models import Value

def inspection_create (request, pk=None):
    if request.method == 'POST':
        # get iform for the new inspection
        iform = IForm.objects.get(id=pk)

        # passing the iform id to form so the form knows which fields to show
        form = InspectionForm(request.POST, iform_id=pk)
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
                '''
                obj.business_email = form.cleaned_data[1]
                obj.business_phone = form.cleaned_data['business_phone']
                obj.business_website = form.cleaned_data['business_website']
                '''

                # finally save the object in db
                obj.save()
            return HttpResponseRedirect('/inspection_list')
        else:
            raise Http404 # form = InspectionForm()

    return render(request, 'inspection/inspection_update.html', {'form': InspectionForm(),})
