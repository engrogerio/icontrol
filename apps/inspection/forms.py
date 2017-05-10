# -*- encoding:utf-8 -*-
from django import forms
from apps.inspection.models import Inspection
from apps.iform.models import IForm
from apps.tag.models import Tag


# class InspectionUpdateForm(forms.ModelForm):
#
#     class Meta:
# 	    model = Inspection
# 	    fields = [
#             'iform',
#             'created_when'
# 		]
# 	    labels = {
#             'iform': 'Form',
# 	    }
        # widgets = {
        #     'id': forms.TextInput(attrs={'class':'form-control'}),
        #     #'iform': forms.ModelChoiceField(queryset=IForm.objects.all()), # attrs={'class':'form-control'}),
        #     'tag': forms.TextInput(attrs={'class':'form-control'}),
        # }

import datetime
class InspectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        iform_id = kwargs.pop('iform_id', None)
        tag_list = IForm.objects.get(pk=iform_id).tag.all()
        super(InspectionForm, self).__init__(*args, **kwargs)
        tags = Tag.objects.filter(pk__in=tag_list)
        # TODO: Show the tags on a specific order
        for i, q in enumerate(tags):
            if q.type == q.TEXT:
                self.fields['%s' % q.id] = forms.CharField(max_length=100, label=str(q), )
            elif q.type == q.INTEGER:
                self.fields['%s' % q.id] = forms.IntegerField( label=str(q), )
            elif q.type == q.FLOAT:
                self.fields['%s' % q.id] = forms.DecimalField( label=str(q), )
            elif q.type == q.BOOL:
                self.fields['%s' % q.id] = forms.BooleanField( label=str(q), initial=False )
            elif q.type == q.DATE:
                self.fields['%s' % q.id] = forms.DateField( label=str(q), initial=datetime.date.today)
            elif q.type == q.TIME:
                self.fields['%s' % q.id] = forms.TimeField( label=str(q), )
            elif q.type == q.DATETIME:
                self.fields['%s' % q.id] = forms.DateTimeField( label=str(q), initial=datetime.datetime.today)
