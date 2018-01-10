from app.tag.models import Tag
from app.iform.models import IForm
def add_variable_to_context(request):
    tags = Tag.objects.all().order_by('name')
    iforms = IForm.objects.all().order_by('name')
    return {
        'tags': tags,
        'iforms': iforms
    }