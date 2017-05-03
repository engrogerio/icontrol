# -*- encoding:utf-8 -*-
from django import forms

from apps.iform.models import IForm


class FormForm(forms.ModelForm):

	class Meta:
		model = IForm
		fields = [
            'id',
			'name',
            'tag',
		]
		labels = {
            'id': 'ID',
			'name': 'Name',
            'tag': 'Tags',
		}
		widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'tag': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
		}
