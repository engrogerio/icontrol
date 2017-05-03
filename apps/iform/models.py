# -*- coding: utf-8 -*-

from django.db.models import UUIDField, ManyToManyField, CharField
import uuid
#from apps.tag.models import Tag
from apps.control.models import ControlModel
# Create your models here.


class IForm(ControlModel):

    class Meta:
        db_table='iform'

    id = UUIDField(primary_key=True, default=uuid.uuid4, )  # editable=False)
    name = CharField(max_length=255)
    tag = ManyToManyField('tag.Tag', related_name='iform_tags')

    def __str__(self):
        return self.name
