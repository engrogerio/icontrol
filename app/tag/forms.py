# -*- encoding:utf-8 -*-
from django import forms

from app.tag.models import Tag


class TagForm(forms.ModelForm):

    choices_source = forms.ModelChoiceField(required=False, queryset=Tag.objects.order_by('name'),
    widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Tag
        fields = [
        'parent',
        'name',
        'help_text',
        'type',
        'choices_source',
        'unit',
        'decimal_places',
        'max_length',
        ]
        labels = {
        'parent': 'Parent',
        'name': 'Name',
        'help_text':'Help Text',
        'type': 'Type',
        'choices_source': 'Choices Source',
        'unit': 'Unit',
        'decimal_places': 'Decimal Places',
        'max_length': 'Maximum Length',

        }
        widgets = {
        'parent': forms.Select(attrs={'class':'form-control'}), 
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'help_text': forms.TextInput(attrs={'class':'form-control'}),
        'type': forms.Select(attrs={'class':'form-control'}), 
        'choices_source': forms.Select(attrs={'class':'form-control'}),
        'unit': forms.Select(attrs={'class':'form-control'}),
        'decimal_places': forms.NumberInput(attrs={'class':'form-control'}),
        'max_length': forms.NumberInput(attrs={'class':'form-control'}),

      }
