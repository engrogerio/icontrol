from apps.iform.forms import FormForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.iform.models import IForm


def FormIndex(request):
    return HttpResponse ('Form list')


class FormList(ListView):
    model = IForm
    template_name = 'iform/iform_list.html'
    paginate_by = 6


class FormCreate(CreateView):
    model = IForm
    template_name = 'iform/iform_form.html'
    form_class = FormForm
    success_url = reverse_lazy('iform:iform_list')


class FormUpdate(UpdateView):
    model = IForm
    template_name = 'iform/iform_form.html'
    form_class = FormForm
    success_url = reverse_lazy('iform:iform_list')


class FormDelete(DeleteView):
    model = IForm
    template_name = 'iform/iform_delete.html'
    form_class = FormForm
    success_url = reverse_lazy('iform:iform_list')

