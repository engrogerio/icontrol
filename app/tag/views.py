from app.tag.forms import TagForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig
from app.tag.models import Tag, TagTable
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.tag.filters import TagFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


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
        context['iform'] = 'iForm'
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

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.created_by = instance.user
        instance.save()
        return super(TagCreate, self).form_valid(form)


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'tag/tag_form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.updated_by = instance.user
        instance.save()
        return super(TagUpdate, self).form_valid(form)


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tag/tag_delete.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag_list')


class FilteredTagView(SingleTableMixin, FilterView):
    table_class = TagTable
    model = Tag
    template_name = 'tag_list.html'

    filterset_class = TagFilter