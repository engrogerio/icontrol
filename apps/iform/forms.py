# -*- encoding:utf-8 -*-
from django import forms

from apps.iform.models import IForm, TagOrder


class IFormForm(forms.ModelForm):

	class Meta:
		model = IForm
		fields = [
			'name',
            'tag',
		]
		labels = {
			'name': 'Name',
            'tag': 'Tags',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'tag': forms.CheckboxSelectMultiple(),
		}
