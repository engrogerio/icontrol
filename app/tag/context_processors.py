# -*- coding: utf-8 -*-
from app.tag.models import Tag
from app.iform.models import IForm
from django.core import serializers
import json


def add_variable_to_context(request):
    tags = Tag.objects.all()
    iforms = IForm.objects.all()
    tags_list = []
    # Add main menu branches
    # Tags:
    #tags_list.append({"id": "1", "text": "Tags", "icons": "fa-tag"})
    for tag in tags:
        parent_id = '#'
        if tag.parent: parent_id=str(tag.parent.id)
        js_tag={"id":str(tag.id), "parent":parent_id, "text":tag.name, "a_attr": {"href": "/tag/update/"+str(tag.id)}}
        tags_list.append(js_tag)
    print(tags_list)
    return {
        'tags': json.dumps(tags_list),
        'iforms': iforms,
    }


