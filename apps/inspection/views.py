from apps.inspection.forms import InspectionForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from apps.inspection.models import Inspection


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

def inspection_create (request):
    print(request)
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            # creates a new inspection based on a iform
            inspection = Inspection()

            # creates a new tag
            obj = Value()
            for field in form:
                obj.text = field.cleaned_data
            '''
            obj.business_email = form.cleaned_data[1]
            obj.business_phone = form.cleaned_data['business_phone']
            obj.business_website = form.cleaned_data['business_website']
            '''

            # finally save the object in db
            obj.save()
            return HttpResponseRedirect('/inspection_list')
        else:
            form = InspectionForm()

    return render(request, 'inspection/inspection_update.html', {'form': InspectionForm()})
