# -*- encoding:utf-8 -*-
from django import forms
from django.forms import formset_factory
from apps.iform.models import IForm, IFormTag

#TagOrder


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

	order = forms.ChoiceField(choices=((str(x), x) for x in range(1,20)))
	formset = formset_factory(IFormTag, extra=2) #, fields=('order', 'read_only'))

	class Meta:
		model = IForm
		fields = [
			'name',
            #'tag',
			'order',

		]
		labels = {
			'name': 'Name',
            #'tag': 'Tags',
			'order': 'Order',
		}
		help_texts = {
		'name': ('Type in the name of the Form'),
		}
		error_messages = {
			'name': {
				'max_length': ("This name is too long."),
			}
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			#'tag': forms.CheckboxSelectMultiple(),
			'order': forms.ChoiceField(choices=((str(x), x) for x in range(1,32))),
		}


    #
	# def __init__(self):
	# 	tag_order = self.name
	# 	#self.fields['tag'] = TagFormField(attrs={'qtty': tag_order, })