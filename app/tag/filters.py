from django_filters import FilterSet
from .models import Tag, TagTable


class TagFilter(FilterSet):
    class Meta:
        model = Tag
        fields = {
            'name': ['exact', 'contains'],
            }
