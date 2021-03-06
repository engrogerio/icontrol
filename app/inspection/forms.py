# -*- coding: utf-8 -*-

from django import forms
from app.inspection.models import Inspection
from app.iform.models import IForm, IFormTag
from app.tag.models import Tag
from app.value.models import Value
from django.forms.models import inlineformset_factory


# TODO: shoud I use validators? https://docs.djangoproject.com/en/1.11/ref/validators/
# TODO: should I use widgets instead of form.Fields?
class InspectionForm(forms.Form):

    def get_widget(self, tag, iform):
        """
        Passing a Tag and an Iform will return the correct widget based on Tag spec
        """

        iform_tag = IFormTag.objects.filter(iform=iform).get(tag=tag)
        attrs = dict()
        if tag.max_length == 0:
            tag.max_length = 1000
        if iform_tag.width > 0:
            attrs = {
                'style': 'width:'+str(iform_tag.width)
            }
        if iform.layout == 1:
            attrs['placeholder'] = tag.name
        # put an asterisc before the tag label when it's a required field
        tag_label = f"{'*' if iform_tag.required else ''} {str(tag)}"

        widget_parameters = {
            'label': tag_label,
            'required': iform_tag.required,
            'initial': iform_tag.default_value,
            'help_text': tag.help_text,
            'disabled': iform_tag.read_only,
        }
        if tag.type == tag.TEXT:
            attrs.update({'max_length':tag.max_length})
            return forms.CharField(
                widget=forms.TextInput(attrs=attrs),
                **widget_parameters
            )
        elif tag.type == tag.LARGE_TEXT:
            attrs.update({'rows':4})
            attrs.update({'max_length':tag.max_length})
            return forms.CharField(
            widget=forms.Textarea(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.INTEGER:
            return forms.IntegerField(
            widget=forms.NumberInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.FLOAT:
            return forms.DecimalField(
            widget=forms.NumberInput(attrs=attrs),
            decimal_places=tag.decimal_places,
            **widget_parameters
            )
        elif tag.type == tag.BOOL:
            return forms.BooleanField(
            **widget_parameters
            )
        elif tag.type == tag.DATE:
            return forms.DateField(
            widget=forms.DateInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.TIME:
            return forms.TimeField(
            widget=forms.TimeInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.DATETIME:
            return forms.DateTimeField(
            widget=forms.DateTimeInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.CHOICES:
            choices=[]
            # bring all options based on all values for the tag choosen on choices_source 
            values = Value.objects.filter(tag=tag.choices_source).exclude(text__exact='').order_by('text') #.values_list('text')
            for n,v in enumerate(values):choices.append([n,v])
            return forms.ChoiceField(
            widget=forms.Select(attrs=attrs),
            choices=choices,
            **widget_parameters
            )
        elif tag.type == tag.RADIO:
            choices=[]
            # bring all options based on values for the tag choosen on choices_source 
            values = Value.objects.filter(tag=tag.choices_source).exclude(text__exact='').order_by('text') #.values_list('text')
            for n, v in enumerate(values):choices.append([n,v])
            return forms.ChoiceField(
            choices=choices,
            widget=forms.RadioSelect(attrs=attrs),
            **widget_parameters
            )
        #TODO make a multiple checked boxes persisted as separated values or a text field like ('value1, value2, value5') ?
        elif tag.type == tag.CHECKBOX:
            choices=[]
            # bring all options based on values for the tag choosen on choices_source 
            values = Value.objects.filter(tag=tag.choices_source).exclude(text__exact='').order_by('text') #.values_list('text')
            for n, v in enumerate(values):choices.append([n,v])
            return forms.MultipleChoiceField(
            choices=choices,
            widget=forms.CheckboxSelectMultiple(attrs=attrs),
            **widget_parameters
            )
        # elif tag.type == tag.MONEY:
        # self.fields['%s' % tag.id] = MoneyField(
            # label=str(tag),
            # required=iform_tag.required,
            # disabled=iform_tag.read_only,
            # initial=iform_tag.default_value,
            # )

        elif tag.type == tag.FILE:
            return forms.ImageField(
            **widget_parameters
            )
            
        elif tag.type == tag.SECTION:
            attrs.update({
                    'iframe':'border: none',
                    'style':'height:2; font-size: 1; background-color: #eeeeee; border: 0; box-shadow: none',
                })
            return forms.CharField(
            label='',
            required=False,
            disabled=True,
            initial=tag.name,
            widget=forms.TextInput(attrs=attrs),
            help_text=tag.name
            )
            
        elif tag.type == tag.URL:
            print(attrs)
            return forms.URLField(
            widget=forms.URLInput(attrs=attrs),
            **widget_parameters
            )

    def __init__(self, *args, **kwargs):
        iform_id = kwargs.pop('iform_id', None)
        iform = IForm.objects.get(id=iform_id)
        tag_list = IForm.objects.get(pk=iform_id).iform_tag.all().values('tag')
        tags = Tag.objects.filter(pk__in=tag_list).filter(
            iform_tag_tag__iform=iform).order_by('iform_tag_tag__order')
        super(InspectionForm, self).__init__(*args, **kwargs)
        # Loop for assembling the form
        for i, tag in enumerate(tags):
            self.fields['%s' % tag.id] = self.get_widget(tag, iform)
