# -*- encoding:utf-8 -*-
from django import forms

from apps.tag.models import Tag


class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = [
            'id',
            'name',
            'type',
            'unit',
            'decimal_places',
		]
		labels = {
            'id': 'ID',
            'name': 'Tag Name',
            'type': 'Tag Type',
            'unit': 'Tag Unit',
            'decimal_places': 'Decimal Places',
		}
		widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}), #widgets=forms.RadioSelect, choices=Tag.TYPE_CHOICES), #attrs={'class':'form-control'}),
            'unit': forms.Select(attrs={'class':'form-control'}), #(attrs={'class':'form-control'}),
            'decimal_places': forms.NumberInput(attrs={'class':'form-control'}),
		}
