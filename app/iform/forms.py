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
            'default_value',
            'width',
            'read_only',
            'required',
        ]
        labels = {
            'tag': 'Name',
            'order': 'Order',
            'read_only': 'Read only',
            'required': 'Required',
            'default_value': 'Default Value',
        }
        help_texts = {
            'order': ('Enter the position of the tag on the form'),
            'tag': ('Choose the tag'),
            'default_value': ('Enter the default value for this tag on this form'),
            'width': ('Enter the width of this field on the form'),
            'read_only': ('Enter the position of the tag on the form'),
            'required': ('Mark if user should enter a value'),
        }
        # error_messages = {
        # 	'tag': {
        # 		'max_length': ("This name is too long."),
        # 	}
        # }
        widgets = {
            'tag': forms.Select(), #attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'style': 'width:100'}),
            #'required': forms.Select(attrs={'class':'form-control'}),
            'default_value': forms.TextInput(attrs={'class':'form-control'}),
            'width': forms.NumberInput(attrs={'style': 'width:100'})
        }


IFormTagFormSet = inlineformset_factory(
    IForm,
    IFormTag,
    IFormForm,
    IFormTagForm,
    fields=('tag', 'order', 'read_only'),
    extra=1,
    can_delete=True)
