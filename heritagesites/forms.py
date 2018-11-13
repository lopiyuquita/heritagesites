from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from heritagesites.models import HeritageSite

#  I want to create a HeritageSiteForm, which is based on HeritageSite model. By using .ModelForm,
# I can "borrow" components from the HeritageSite model to avoid redundancy.

class HeritageSiteForm(forms.ModelForm):
	class Meta:
		model = HeritageSite
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))


