from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from app.tag.models import Tag

class TagAdmin(DjangoMpttAdmin):
    item_label_field_name = 'name'
    tree_auto_open = False
    autoescape = True
    use_context_menu = True

admin.site.register(Tag, TagAdmin)
