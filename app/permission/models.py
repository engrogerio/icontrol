from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def add_permission(inspection_name, type):
    """
    Creates read or write permission for every single Iform. After creating a form 
    for the first time, the groups are created
    """    
    content_type = ContentType.objects.get(app_label='app_name', model='model_name')
    permission = Permission.objects.create(codename='can_create_hr',
                                        name='Can create HR',
                                        content_type=content_type) # creating permissions
    group = Group.objects.get(name='HR')
    group.permissions.add(permission)
