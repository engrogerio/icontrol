from app.tag.models import Tag
from app.iform.models import IForm
from django.core import serializers



def add_variable_to_context(request):
    tags = Tag.objects.all()
    iforms = IForm.objects.all()
    # assuming obj is a model instance
    serialized_tags = serializers.serialize('json', tags,)
    return {
        'tags': serialized_tags,
        'iforms': iforms
    }


