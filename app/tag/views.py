from app.tag.forms import TagForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig
from app.tag.models import Tag, TagTable
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

def TagIndex(request):
    return HttpResponse ('Tag list')


class TagList(LoginRequiredMixin, ListView):
    model = Tag
    context_name = 'tag'
    ordering = ['name']
    queryset = Tag.objects.all()
    table = TagTable(queryset)

    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        table = TagTable(Tag.objects.order_by('-pk')) #filter(self.kwargs['company']).order_by('-pk'))
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

    # RequestConfig(request).configure(table)
    # return render(request, 'tag/tag_list.html', {'table': table})
    # # template_name = 'tag/tag_list.html'
    # # paginate_by = 60


class TagCreate(LoginRequiredMixin, CreateView ):
    model = Tag
    template_name = 'tag/tag_form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')

    # def get_context_data(self, **kwargs):
    # # To get current user
    #     c = super(TagCreate, self).get_context_data(**kwargs)
    #     self user = self.request.user
    #     return c

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(TagCreate, self).form_valid(form)

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'tag/tag_form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tag/tag_delete.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')
