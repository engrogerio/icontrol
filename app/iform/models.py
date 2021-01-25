# -*- coding: utf-8 -*-

from django.db.models import UUIDField, ManyToManyField, CharField, IntegerField, ForeignKey, BooleanField
import uuid

from django.forms.fields import ChoiceField
from icontrol.models import ControlModel
from django.db import models


class IForm(ControlModel):

    NORMAL = 0
    INLINE = 1
    FIXED = 0
    COLLAPSIBLEOPEN = 1
    COLLAPSIBLECLOSED = 2
    LAYOUT = ((NORMAL, 'Normal'), (INLINE, 'Inline'))
    COLLAPSIBLE = ((FIXED, 'Fixed'), (COLLAPSIBLEOPEN, 'Default Opened'), (COLLAPSIBLECLOSED, 'Default Closed'))


    class Meta:
        db_table = 'iform'

    id = UUIDField(primary_key=True, default=uuid.uuid4,)
    name = CharField(max_length=255, default='New Form')
    parent = ForeignKey('self', blank=True, null=True, related_name='children', 
                        db_index=True, on_delete=models.CASCADE)
    collapsible = IntegerField(choices=COLLAPSIBLE, default=FIXED)
    layout = IntegerField(choices=LAYOUT, default=NORMAL)

    def __str__(self):
        return self.name


class IFormTag(ControlModel):

    class Meta:
        db_table= 'iform_tag'
        # every tag must appears only once on one form
        unique_together = ["iform", "tag"]

    iform = ForeignKey(IForm, related_name='iform_tag', on_delete=models.CASCADE) 
    tag = ForeignKey('tag.Tag', related_name='iform_tag_tag', on_delete=models.CASCADE)
    order = IntegerField(default=1) # TODO: This must be automatically increased
    read_only = BooleanField(default=False)
    required = BooleanField(default=False)
    default_value = CharField(max_length=1000, null=True, blank=True)
    width = IntegerField(default=0)