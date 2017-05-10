# -*- coding: utf-8 -*-

from django.db.models import UUIDField, ManyToManyField, CharField, IntegerField, ForeignKey
import uuid
from apps.control.models import ControlModel
from django.db import models


# Create your models here.


class IForm(ControlModel):

    class Meta:
        db_table='iform'

    id = UUIDField(primary_key=True, default=uuid.uuid4, )  # editable=False)
    name = CharField(max_length=255)
    tag = ManyToManyField('tag.Tag', related_name='iform_tags', through = 'TagOrder')

    def __str__(self):
        return self.name

class TagOrder(models.Model):

    class Meta:
        auto_created = True

    iform = ForeignKey(IForm, related_name='tag_order')
    tag = ForeignKey('tag.Tag', related_name='tag_order')
    order = IntegerField(default=1)

