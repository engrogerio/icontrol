# from django.contrib import admin
# from django import forms
# from app.iform.models import IForm, IFormTag
# # Register your models here.
#
# class IFormForm(forms.ModelForm):
#     class Meta:
#         model = IForm
#         fields = ('name', 'parent', )
#
#
# class IFormTagInline(admin.TabularInline):
#     model = IFormTag
#     #formset = ItemInlineFormSet
#     extra = 0
#     fields = ['tag','order','read_only']
#
#
# class IFormAdmin(admin.ModelAdmin):
#     form = IFormForm
#     inlines = [IFormTagInline]
#     list_display = ('name',)
#
# admin.site.register(IForm, IFormAdmin,)
#
