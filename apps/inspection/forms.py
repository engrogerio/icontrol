# -*- encoding:utf-8 -*-
from django import forms

from apps.inspection.models import Inspection
from apps.iform.models import IForm
from apps.tag.models import Tag


class InspectionForm(forms.ModelForm):

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
            'tag': forms.TextInput(attrs={'class':'form-control'}),
        }

class InspectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        iform_id = kwargs.pop('iform_id', None)
        print('iform_id',iform_id )

        super(InspectionForm, self).__init__(*args, **kwargs)
        tags = Tag.objects.all()
        # TODO: Show the tags on a specific order
        for i, q in enumerate(tags):
            self.fields['%s' % q.id] = forms.CharField(max_length=100, label=str(q), )

