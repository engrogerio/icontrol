from apps.iform.forms import IFormForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apps.iform.models import IForm, IFormTag
#from apps.iform.forms import IFormTagFormSet

def IFormIndex(request):
    return HttpResponse ('Form list')


class IFormList(ListView):
    model = IForm
    template_name = 'iform/iform_list.html'
    paginate_by = 6

#
# class IFormCreate(CreateView):
#     model = IForm
#     template_name = 'iform/iform_form.html'
#     form_class = IFormForm
#     success_url = reverse_lazy('iform:iform_list')
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         # get tags fields
#         tag_uids = form['tag']
#         tag_id = form['id']
#         iform=form.instance
#         # get quantity of tags that may be selected for the positioning index (order)
#         position = 0
#         # iter each tag, fill the values and save it.
#         for id in tag_id.value():
#             # value = id['tag']
#             print('value--->>>', id)
#             position = position + 1
#             tag = Tag.objects.get(id=id['tag'].value())
#             # creates a new iform_tag (m2m field)
#             iform_tag = IFormTag()
#             iform_tag.tag = tag
#             iform_tag.iform = iform
#             #iform_tag.order = position
#             iform_tag.save()
#
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#
# class IFormUpdate(UpdateView):
#     model = IForm
#     template_name = 'iform/iform_form.html'
#     form_class = IFormForm
#     success_url = reverse_lazy('iform:iform_list')
#
#
#     def form_valid(self, form):
#
#         self.object = form.save(commit=True)
#         # get tags fields
#         tag_ids = form['iform_tag']
#         iform = form.instance
#         # get quantity of tags that may be selected for the positioning index (order)
#         position = 0
#         # iter each tag, fill the values and save it.
#         for id in tag_ids.value():
#             tag = Tag.objects.get(id=id)
#             # gets the instance of iform_tag based on the iform and the tag
#             iform_tag = IFormTag.objects.filter(iform=iform).get(tag=tag)
#             iform_tag.order = position
#             iform_tag.save()
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())