from apps.iform.forms import IFormForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
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


    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     for field in form:
    #         print(type(self.object))
    #
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


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
#
#
# def add_iform_tag(request):
#     form = IFormForm(request.POST or None)
#     if form.is_valid():
#         iform = IForm.objects.create()
#
#
# def iform_create(request):
#     pass
#
# def iform_update(request, pk=None):
#     pass
