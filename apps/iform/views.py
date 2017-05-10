from apps.iform.forms import IFormForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.iform.models import IForm


def IFormIndex(request):
    return HttpResponse ('Form list')


class IFormList(ListView):
    model = IForm
    template_name = 'iform/iform_list.html'
    paginate_by = 6


class IFormCreate(CreateView):
    model = IForm
    template_name = 'iform/iform_form.html'
    form_class = IFormForm
    success_url = reverse_lazy('iform:iform_list')


class IFormUpdate(UpdateView):
    model = IForm
    template_name = 'iform/iform_form.html'
    form_class = IFormForm
    success_url = reverse_lazy('iform:iform_list')


class IFormDelete(DeleteView):
    model = IForm
    form_class = IFormForm
    template_name = 'iform/iform_delete.html'
    success_url = reverse_lazy('iform:iform_list')

