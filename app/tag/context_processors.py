from app.tag.models import Tag
from app.iform.models import IForm


def add_variable_to_context(request):
    tags = Tag.objects.all()
    iforms = IForm.objects.all()

    return {
        'tags': tags,
        'iforms': iforms
    }


