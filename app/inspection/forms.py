# -*- coding: utf-8 -*-

from django import forms
from app.iform.models import IForm, IFormTag
from app.tag.models import Tag
from app.value.models import Value
import datetime


# TODO: shoud I use validators? https://docs.djangoproject.com/en/1.11/ref/validators/
# TODO: should I use widgets instead of form.Fields?
        
class InspectionForm(forms.Form):

    def get_widget(self, tag, iform):
        """
        Passing a Tag and an Iform will return the correct widget based on Tag spec
        """
        iform_tag=IFormTag.objects.filter(iform=iform).get(tag=tag)
        attrs = dict()
        if tag.max_length==0:tag.max_length=1000

        # put an asterisc after the tag label when it's a required field
        tag_label = str(tag) if not iform_tag.required else str(tag)+' *'

        widget_parameters = {
            'label': tag_label,
            'required': iform_tag.required,
            'max_length': tag.max_length,
            'initial': iform_tag.default_value,
            'help_text': tag.help_text,
            'disabled': iform_tag.read_only, 
            #'placeholder': 'placeholder'
        }
        
        if tag.type == tag.TEXT:
            return forms.CharField(
            widget=forms.TextInput(attrs=attrs), 
            **widget_parameters
            )
        elif tag.type == tag.LARGE_TEXT:
            attrs.update({'rows':4})
            return forms.CharField(
            widget=forms.Textarea(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.INTEGER:
            widget_parameters.pop('max_length')
            return forms.IntegerField(
            widget=forms.NumberInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.FLOAT:
            widget_parameters.pop('max_length')
            return forms.DecimalField(
            widget=forms.NumberInput(attrs=attrs),
            decimal_places=tag.decimal_places,
            **widget_parameters
            )
        elif tag.type == tag.BOOL:
            widget_parameters.pop('max_length')
            return forms.BooleanField(
            **widget_parameters
            )
        elif tag.type == tag.DATE:
            widget_parameters.pop('max_length')
            return forms.DateField(
            widget=forms.DateInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.TIME:
            widget_parameters.pop('max_length')
            return forms.TimeField(
            widget=forms.TimeInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.DATETIME:
            widget_parameters.pop('max_length')
            return forms.DateTimeField(
            widget=forms.DateTimeInput(attrs=attrs),
            **widget_parameters
            )
        elif tag.type == tag.CHOICES:
            choices=[]
            widget_parameters.pop('max_length')
            # bring all options based on all values for the tag choosen on choices_source 
            values = Value.objects.filter(tag=tag.choices_source).exclude(text__exact='').order_by('text') #.values_list('text')
            print(values)
            for n,v in enumerate(values):
                choices.append([n,v])
                print(type(v))
            return forms.ChoiceField( 
            widget=forms.Select(attrs=attrs),
            choices= choices,
            **widget_parameters
            )        
        elif tag.type == tag.RADIO:
            choices=[]
            widget_parameters.pop('max_length')
            # bring all options based on all values for the tag choosen on choices_source 
            values = Value.objects.filter(tag=tag.choices_source).exclude(text__exact='').order_by('text') #.values_list('text')
            for n,v in enumerate(values):choices.append([n,v])
            return forms.ChoiceField(
            choices= choices,
            widget=forms.RadioSelect(attrs=attrs),
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
            widget_parameters.pop('max_length')
            return forms.ImageField(
            **widget_parameters
            )    
        elif tag.type == tag.SECTION:
            widget_parameters.pop('max_length')
            attrs.update({
                    'iframe':'border: none',
                    'style':'height:50; font-size: 25; background-color: #ffffff; border: 0; box-shadow: none',
                })
            return forms.CharField(
            label='',
            required=False,
            disabled=True,
            initial=tag.name,
            widget=forms.TextInput(attrs=attrs)
            )

    def __init__(self, *args, **kwargs):
        iform_id = kwargs.pop('iform_id', None)
        iform = IForm.objects.get(id=iform_id)
        tag_list = IForm.objects.get(pk=iform_id).iforms.all().values('tag')
        tags = Tag.objects.filter(pk__in=tag_list).filter(
            iform_tags__iform=iform).order_by('iform_tags__order')
        super(InspectionForm, self).__init__(*args, **kwargs)
        print('Tags ****',tags)
        #Loop for assembling the form. Disregard folders 
        for i, tag in enumerate(tags):
            self.fields['%s' % tag.id] = self.get_widget(tag, iform)
