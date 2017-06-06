# -*- encoding:utf-8 -*-
from django import forms
from apps.inspection.models import Inspection
from apps.iform.models import IForm, IFormTag
from apps.tag.models import Tag
import datetime

# TODO: shoud I use validators? https://docs.djangoproject.com/en/1.11/ref/validators/
# TODO: should I use widgets instead of form.Fields?

class InspectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        iform_id = kwargs.pop('iform_id', None)
        iform = IForm.objects.get(id=iform_id)
        tag_list = IForm.objects.get(pk=iform_id).iform_tag.all().values('tag')
        tags = Tag.objects.filter(pk__in=tag_list).filter(iform_tag__iform=iform).order_by('iform_tag__order')
        super(InspectionForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(tags):
            iform_tag=IFormTag.objects.filter(iform=iform).get(tag=q)
            if q.type == q.TEXT:
                if not q.max_length:q.max_length=1000
                self.fields['%s' % q.id] = forms.CharField(
                                                label=str(q),
                                                required=q.required,
                                                max_length=q.max_length
                                                )

            elif q.type == q.INTEGER:
                self.fields['%s' % q.id] = forms.IntegerField(label=str(q),
                                                              required=q.required,
                                                              disabled=iform_tag.read_only
                                                              )
            elif q.type == q.FLOAT:
                self.fields['%s' % q.id] = forms.DecimalField(label=str(q),
                                                              required=q.required,
                                                              disabled=iform_tag.read_only
                                                              )
            elif q.type == q.BOOL:
                self.fields['%s' % q.id] = forms.BooleanField(label=str(q),
                                                                required=q.required,
                                                                disabled = iform_tag.read_only
                                                              )
            elif q.type == q.DATE:
                self.fields['%s' % q.id] = forms.DateField(label=str(q),
                                                           required=q.required,
                                                           disabled=iform_tag.read_only
                                                           )
            elif q.type == q.TIME:
                self.fields['%s' % q.id] = forms.TimeField(label=str(q),
                                                           required=q.required,
                                                           disabled=iform_tag.read_only
                                                           )
            elif q.type == q.DATETIME:
                self.fields['%s' % q.id] = forms.DateTimeField(label=str(q),
                                                               required=q.required,
                                                               disabled=iform_tag.read_only
                                                               )
