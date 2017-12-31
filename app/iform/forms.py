# -*- encoding:utf-8 -*-
from django import forms
from django.forms import formset_factory
from app.iform.models import IForm, IFormTag
from app.tag.models import Tag
from django.forms.models import inlineformset_factory


class IFormForm(forms.ModelForm):
    # parent = forms.ModelChoiceField(queryset=IForm.objects.order_by('parent'))

    def __init__(self, *args, **kwargs):
        iform_id = kwargs.pop('iform_id', None)
        super(IFormForm, self).__init__(*args, **kwargs)
        # self.fields['units'] = forms.ModelMultipleChoiceField(
        # 	required=False,
        # 	queryset=IForm.objects.filter(id=iform_id),
        # 	widget=forms.SelectMultiple(attrs={'title': _("Add unit")})
        # )

    class Meta:
        model = IForm
        # exclude = ('created_by', 'created_when', 'id')
        fields = [
            'name',
            'parent'
        ]
        # labels = {
        # 	'name': 'Name',
        #    'parent': 'Parent'
        # }
        # 	help_texts = {
        # 	'name': ('Type in the name of the Form'),
        # 	}
        # 	error_messages = {
        # 		'name': {
        # 			'max_length': ("This name is too long."),
        # 		}
        # 	}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),

        }


class IFormTagForm(forms.ModelForm):

    tag = forms.ModelChoiceField(queryset=Tag.objects.order_by('name'))

    class Meta:
        model = IFormTag
        exclude = ('created_by', 'created_when', 'id')

        fields = [
            'order',
            'tag',
            'read_only',
            'required',
            'default_value',
        ]
        labels = {
            'tag': 'Name',
            'order': 'Order',
            'read_only': 'Read only',
            'required': 'Is required',
            'default_value': 'Default Value',
        }
        help_texts = {
            'order': ('Enter the position of the tag on the form'),
        }
        # error_messages = {
        # 	'tag': {
        # 		'max_length': ("This name is too long."),
        # 	}
        # }
        widgets = {
            'tag': forms.Select(), #attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'size': 2}),
            #'required': forms.Select(attrs={'class':'form-control'}),
            'default_value': forms.TextInput(attrs={'class':'form-control'}),
        }


IFormTagFormSet = inlineformset_factory(
    IForm,
    IFormTag,
    IFormForm,
    IFormTagForm,
    fields=('tag', 'order', 'read_only'),
    extra=1,
    can_delete=True)
