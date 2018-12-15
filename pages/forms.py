from django import forms

valve_type = (
	(0, 'Ball'),
	(1, 'Butterfly')
)

class TestForm(forms.Form):
	days = forms.ChoiceField(choices=valve_type, widget=forms.Select(attrs={
		'class': 'form-control',
		'id': 'inputState',
		#'rows': '3',
		}))


	    # days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])