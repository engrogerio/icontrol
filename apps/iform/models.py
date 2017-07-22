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
    name = CharField(max_length=255, default='New Form')
    parent = ForeignKey('iform.IForm', null=True, blank=True)

    def __str__(self):
        return self.name


class IFormTag(models.Model):

    class Meta:
        db_table='iform_tag'

    iform = ForeignKey(IForm, related_name='iform_tag')
    tag = ForeignKey('tag.Tag', related_name='iform_tag')
    order = IntegerField(default=1) # TODO: This must be automatically increased
    read_only = BooleanField(default=False)


    class Meta:
        # every tag must appears only once on one form
        unique_together = ["iform", "tag"]