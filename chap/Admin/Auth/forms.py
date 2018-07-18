from django import forms
from .import models
class AddDb(forms.ModelForm):
	class Meta:
		model=models.Uploaddb
		fields=['title','file']