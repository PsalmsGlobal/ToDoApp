from django import forms
from .models import MyList

class MyListForm(forms.ModelForm):
	class Meta:
		model = MyList
		fields = ["item", "completed"]