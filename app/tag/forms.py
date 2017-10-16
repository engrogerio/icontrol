# -*- encoding:utf-8 -*-
from django import forms

from app.tag.models import Tag


class TagForm(forms.ModelForm):

    choices_source = forms.ModelChoiceField(required=False, queryset=Tag.objects.order_by('name'),
    widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Tag
        fields = [
        'name',
        'type',
        'choices_source',
        'unit',
        'decimal_places',
        'max_length',
        'required'
        ]
        labels = {
        'name': 'Name',
        'type': 'Type',
        'choices_source': 'Choices Source',
        'unit': 'Unit',
        'decimal_places': 'Decimal Places',
        'max_length': 'Maximum Length',
        'required': 'Is required',
        }
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'type': forms.Select(attrs={'class':'form-control'}), 
        #'choices_source': forms.Select(attrs={'class':'form-control'}),
        'unit': forms.Select(attrs={'class':'form-control'}),
        'decimal_places': forms.NumberInput(attrs={'class':'form-control'}),
        'max_length': forms.NumberInput(attrs={'class':'form-control'}),
        'required': forms.Select(attrs={'class':'form-control'}),
      }
