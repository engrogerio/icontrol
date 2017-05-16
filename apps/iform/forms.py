# -*- encoding:utf-8 -*-
from django import forms

from apps.iform.models import IForm
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

	class Meta:
		model = IForm
		fields = [
			'name',
            'tag',
		]
		labels = {
			'name': 'Name',
            'tag': 'Tags',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'tag': forms.CheckboxSelectMultiple(),

		}
    #
	# def __init__(self):
	# 	tag_order = self.name
	# 	#self.fields['tag'] = TagFormField(attrs={'qtty': tag_order, })