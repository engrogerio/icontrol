# -*- coding: utf-8 -*-

from django.db.models import UUIDField, ManyToManyField, CharField, IntegerField, ForeignKey, BooleanField
import uuid
from icontrol.models import ControlModel
from django.db import models

# Create your models here.
class IForm(ControlModel):

    class Meta:
        db_table='iform'

    id = UUIDField(primary_key=True, default=uuid.uuid4,)
    name = CharField(max_length=255, default='New Form')
    parent = parent = ForeignKey('self', on_delete = models.CASCADE, 
                                blank=True, null=True, related_name='children', db_index=True,)

    def __str__(self):
        return self.name


class IFormTag(models.Model):

    class Meta:
        db_table='iform_tag'
        # every tag must appears only once on one form
        unique_together = ["iform", "tag"]

    iform = ForeignKey(IForm, related_name='iforms', on_delete = models.CASCADE, ) 
    tag = ForeignKey('tag.Tag', related_name='iform_tags', on_delete = models.CASCADE, )
    order = IntegerField(default=1) # TODO: This must be automatically .increased
    read_only = BooleanField(default=False)
    required = BooleanField(default=False)
    default_value = CharField(max_length=1000, null=True, blank=True)
    # width = IntegerField(default=0)

  