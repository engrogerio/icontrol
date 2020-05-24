# -*- coding: utf-8 -*-
from app.tag.models import Tag
from app.iform.models import IForm, IFormTag
from app.inspection.models import Inspection
from django.core import serializers
import json


def add_tree_menu_to_context(request):
    tags = Tag.objects.all().order_by('name')
    iforms = IForm.objects.all().order_by('name')
    iformtags = IFormTag.objects.all().order_by('order')
    inspections = Inspection.objects.all().order_by('iform','created_when')
    obj_list = []

    # Creating branch for editing options

    #creating branch for create new tags
    inspection_branch = {"id": "new_tags", "parent": "#", "text": " New Tag", "icon": "fa fa-tags",
        "a_attr": {"href": "/tag/create"}}
    obj_list.append(inspection_branch)

    # #creating branch for tags
    # inspection_branch = {"id":"tags", "parent":"#", "text":"Edit Tag", "icon": "fa fa-tag",
    #     "a_attr":{"href":"/tag/list"}}
    # obj_list.append(inspection_branch)

    #creating branch for create new iforms
    inspection_branch = {"id": "new_iforms", "parent": "#", "text": " New Form", "icon": "fa fa-eye",
        "a_attr": {"href": "/iform/create"}}
    obj_list.append(inspection_branch)

    #creating branch for iforms
    inspection_branch = {"id": "iforms", "parent": "#", "text": " Edit Form", "icon": "fa fa-list"}
    obj_list.append(inspection_branch)

    #creating branch for create new inspections
    inspection_branch = {"id": "new_inspection", "parent": "#", "text": " New Inspection", "icon": "fa fa-search-plus"}
    obj_list.append(inspection_branch)

    #creating branch for showing inspections values
    inspection_branch = {"id": "show_values", "parent": "#", "text": " Show Data Collections", "icon": "fa fa-camera"}
    obj_list.append(inspection_branch)

    #creating branch for inspections
    inspection_branch = {"id": "inspections", "parent": "#", "text": " Edit Inspection", "icon": "fa fa-file"}
    obj_list.append(inspection_branch)


    #Inserting iForm editions
    for iform in iforms:
        parent_id = 'iforms'
        if iform.parent: parent_id=str(iform.parent.id)
        js_iform={"id": str(iform.id), "parent": parent_id, "text": iform.name, "icon": "fa fa-list",
            "a_attr": {"href": "/iform/update/"+str(iform.id)}}
        obj_list.append(js_iform)
        #Inserting tags on iforms
        for iformtag in iformtags.filter(iform=iform):
            parent_id = 'iforms'
            if iformtag.iform: parent_id=str(iformtag.iform.id)
            js_iformtag={"id": str(iformtag.id), "parent": parent_id, "text": iformtag.tag.name, "icon": "fa fa-tag",
                "a_attr": {"href": "/tag/update/"+str(iformtag.tag.id)}}
            obj_list.append(js_iformtag)
        
    #Inserting create new inspections
    for form in iforms:
        fparent_id = 'new_inspection'
        if form.parent: fparent_id=str(form.parent.id)+'new'
        js_form={"id": str(form.id)+'new', "parent": fparent_id, "text": form.name, "icon": "fa fa-search-plus",
            "a_attr": {"href": "/inspection/create/"+str(form.id)}}
        obj_list.append(js_form)

    #Inserting show data collections
    for form in iforms:
        fparent_id = 'show_values'
        if form.parent: fparent_id=str(form.parent.id)+'show'
        js_form={"id": str(form.id)+'show', "parent": fparent_id, "text": form.name, "icon": "fa fa-camera",
        "a_attr": {"href": "/inspection/values/"+str(form.id)}}
        obj_list.append(js_form)

    #Inserting edit inspection
    for inspection in inspections:
        js_inspection={"id": str(inspection.id), "parent":"inspections",
        "text": str(inspection), "icon": "fa fa-file",
        "a_attr": {"href": "/inspection/update/"+str(inspection.id)}}
        obj_list.append(js_inspection)
        
    return {
        'tags': json.dumps(obj_list),
        'iforms': iforms,
    }


