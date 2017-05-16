# -*- encoding:utf-8 -*-
from django import forms
from apps.inspection.models import Inspection
from apps.iform.models import IForm
from apps.tag.models import Tag
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
                if not q.max_length:q.max_length=1000
                self.fields['%s' % q.id] = forms.CharField(label=str(q), required=False, max_length=q.max_length, )
            elif q.type == q.INTEGER:
                self.fields['%s' % q.id] = forms.IntegerField(label=str(q), )
            elif q.type == q.FLOAT:
                self.fields['%s' % q.id] = forms.DecimalField(label=str(q), )
            elif q.type == q.BOOL:
                self.fields['%s' % q.id] = forms.BooleanField(label=str(q), required=False )
            elif q.type == q.DATE:
                self.fields['%s' % q.id] = forms.DateField(label=str(q), )
            elif q.type == q.TIME:
                self.fields['%s' % q.id] = forms.TimeField(label=str(q), )
            elif q.type == q.DATETIME:
                self.fields['%s' % q.id] = forms.DateTimeField(label=str(q), )
