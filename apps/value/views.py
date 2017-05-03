from control.forms import TagForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.tag.models import Tag


def TagIndex(request):
    return HttpResponse ('Tag list')


class TagList(ListView):
    model = Tag
    template_name = 'tag/tag_list.html'
    paginate_by = 2


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


#Templates
class TemplateList(ListView):
    model = Template
    template_name = 'template/template_list.html'
    paginate_by = 2


class TemplateCreate(CreateView):
    model = Template
    template_name = 'template/template_form.html'
    form_class = TagForm
    success_url = reverse_lazy('template:template_list')


class TemplateUpdate(UpdateView):
    model = Template
    template_name = 'template/template_form.html'
    form_class = TagForm
    success_url = reverse_lazy('template:template_list')


class TemplateDelete(DeleteView):
    model = Template
    template_name = 'template/template_delete.html'
    form_class = TagForm
    success_url = reverse_lazy('template:template_list')
''

#Inspections
class InspectionList(ListView):
    model = Inspection
    template_name = 'inspection/inspection_list.html'
    paginate_by = 2


class InspectionCreate(CreateView):
    model = Inspection
    template_name = 'inspection/inspection_form.html'
    form_class = TagForm
    success_url = reverse_lazy('inspection:inspection_list')


class InspectionUpdate(UpdateView):
    model = Inspection
    template_name = 'inspection/inspection_form.html'
    form_class = TagForm
    success_url = reverse_lazy('inspection:inspection_list')


class InspectionDelete(DeleteView):
    model = Inspection
    template_name = 'inspection/inspection_delete.html'
    form_class = TagForm
    success_url = reverse_lazy('inspection:inspection_list')
