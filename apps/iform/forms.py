# -*- encoding:utf-8 -*-
from django import forms
from django.forms import formset_factory
from apps.iform.models import IForm, IFormTag
from django.forms.models import inlineformset_factory



# class TagFormWidget(forms.MultiWidget):
#
#     def __init__(self, attrs=None):
#         self.qtd_pallets = attrs['qtty']
#         attrs['size'] = 5
#         widgets = [forms.TextInput(attrs), forms.TextInput(attrs)]
#         super(TagFormWidget, self).__init__(widgets, attrs)
#
#     def decompress(self, value):
#         if value:
#             return value.split(',')
#         return ['']*self.qtd_pallets


# class TagFormField(forms.fields.MultiValueField):
#
#     def __init__(self, attrs=None):
#         self.widget = TagFormWidget(attrs)
#         fields = [forms.fields.CharField(), forms.fields.IntegerField()]
#         super(TagFormField, self).__init__(fields, attrs)
#
#     def compress(self, values):
#         return ','.join(values)


class IFormForm(forms.ModelForm):

	#formset = formset_factory(IFormTag, extra=2)

	class Meta:
		model = IForm
		exclude=('created_by', 'created_when', 'id')
	# 	fields = [
	# 		'name',
     #        'parent',
	# 	]
	# 	labels = {
	# 		'name': 'Name',
     #        'parent': 'Parent'
	# 	}
	# 	help_texts = {
	# 	'name': ('Type in the name of the Form'),
	# 	}
	# 	error_messages = {
	# 		'name': {
	# 			'max_length': ("This name is too long."),
	# 		}
	# 	}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'parent': forms.Select(attrs={'class': 'form-control'}),

		}

IFormTagFormSet = inlineformset_factory(IForm, IFormTag, form=IFormForm)


	# def __init__(self):
	# 	tag_order = self.name
	# 	#self.fields['tag'] = TagFormField(attrs={'qtty': tag_order, })