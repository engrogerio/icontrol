# -*- coding: utf-8 -*-

from django.db.models import UUIDField, ManyToManyField, CharField, IntegerField, ForeignKey, BooleanField
import uuid
from apps.control.models import ControlModel
from django.db import models


# Create your models here.
class IForm(ControlModel):

    class Meta:
        db_table='iform'

    id = UUIDField(primary_key=True, default=uuid.uuid4,)  # editable=False)
    name = CharField(max_length=255)
    tag = ManyToManyField('tag.Tag', related_name='iform_tags', blank=True)

    def __str__(self):
        return self.name

class IformTag(models.Model):

    def number(self):
        no = IForm.objects.filter().count()
        if no == None:
            return 1
        else:
            return no + 1

    iform = ForeignKey(IForm, related_name='tag_order_form')
    tag = ForeignKey('tag.Tag', related_name='tag_order')
    order = IntegerField(default=number)
    required = BooleanField(default=False)

