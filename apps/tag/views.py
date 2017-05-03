from apps.tag.forms import TagForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.tag.models import Tag


def TagIndex(request):
    return HttpResponse ('Tag list')


class TagList(ListView):
    model = Tag
    template_name = 'tag/tag_list.html'
    paginate_by = 6


class TagCreate(CreateView):
    model = Tag
    template_name = 'tag/tag_form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')


class TagUpdate(UpdateView):
    model = Tag
    template_name = 'tag/tag_form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')


class TagDelete(DeleteView):
    model = Tag
    template_name = 'tag/tag_delete.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')

