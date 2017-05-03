# -*- encoding:utf-8 -*-
from django import forms

from apps.inspection.models import Inspection
from apps.iform.models import IForm
from apps.tag.models import Tag


class InspectionForm(forms.ModelForm):

    for fields in Inspection.objects.all():
        print('-->>',type(fields.iform))

    class Meta:
	    model = Inspection
	    fields = [
            'id',
            'iform',
            'created_when'
		]
	    labels = {
            'id': 'ID',
            'iform': 'Form',
	    }
	    widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            #'iform': forms.ModelChoiceField(queryset=IForm.objects.all()), # attrs={'class':'form-control'}),
            'tag1': forms.TextInput(attrs={'class':'form-control'}),
        }

class InspectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(InspectionForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(Tag.objects.all()):
            self.fields['%s_field' % i] = forms.CharField(max_length=100, label=str(q))

