# -*- coding: utf-8 -*-
from app.tag.models import Tag
from app.iform.models import IForm
from app.inspection.models import Inspection
from django.core import serializers
import json


def add_variable_to_context(request):
    tags = Tag.objects.all().order_by('name')
    iforms = IForm.objects.all().order_by('name')
    inspections = Inspection.objects.all().order_by('iform','created_when')
    obj_list = []


    #creating branch for create new tags
    inspection_branch = {"id":"new_tags", "parent":"#", "text":"Create Tag", "icon": "fa fa-tags",
        "a_attr": {"href": "/tag/create"}}
    obj_list.append(inspection_branch)

    #creating branch for tags
    inspection_branch = {"id":"tags", "parent":"#", "text":"Edit Tag", "icon": "fa fa-tag",
        "a_attr":{"href":"/tag/list"}}
    obj_list.append(inspection_branch)

    #creating branch for create new iforms
    inspection_branch = {"id":"new_iforms", "parent":"#", "text":"Create Form", "icon": "fa fa-eye",
        "a_attr": {"href": "/iform/create"}}
    obj_list.append(inspection_branch)

    #creating branch for iforms
    inspection_branch = {"id":"iforms", "parent":"#", "text":"Edit Form", "icon": "fa fa-list"}
    obj_list.append(inspection_branch)

    #creating branch for create new inspections
    inspection_branch = {"id":"new_inspection", "parent":"#", "text":"Create Inspection", "icon": "fa fa-search-plus"}
    obj_list.append(inspection_branch)

    #creating branch for inspections
    inspection_branch = {"id":"inspections", "parent":"#", "text":"Edit Inspection", "icon": "fa fa-file"}
    obj_list.append(inspection_branch)


    #Inserting Tags edition on Tree menu
    for tag in tags:
        parent_id = 'tags'
        if tag.parent: parent_id=str(tag.parent.id)
        js_tag={"id":str(tag.id), "parent":parent_id, "text":tag.name, "icon": "fa fa-tag",
            "a_attr": {"href": "/tag/update/"+str(tag.id)}}
        obj_list.append(js_tag)

    #Inserting iForm editions
    for iform in iforms:
        parent_id = 'iforms'
        if iform.parent: parent_id=str(iform.parent.id)
        js_iform={"id":str(iform.id), "parent":parent_id, "text":iform.name, "icon": "fa fa-list",
            "a_attr": {"href": "/iform/update/"+str(iform.id)}}
        obj_list.append(js_iform)

   #Inserting create new inspections
    for form in iforms:
        fparent_id = 'new_inspection'
        if form.parent: fparent_id=str(form.parent.id)+'new'
        js_form={"id":str(form.id)+'new', "parent":fparent_id, "text":form.name, "icon": "fa fa-search-plus",
            "a_attr": {"href": "/inspection/create/"+str(form.id)}}
        obj_list.append(js_form)

    #Inserting edit inspection
    for inspection in inspections:
        js_inspection={"id":str(inspection.id), "parent":"inspections", "text":str(inspection)
        , "icon": "fa fa-file",
            "a_attr": {"href": "/inspection/update/"+str(inspection.id)}}
        obj_list.append(js_inspection)

    return {
        'tags': json.dumps(obj_list),
        'iforms': iforms,
    }


