from django import forms

from .models import Module

time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
valid_time_formats = ['%H:%M']

class RegisterForm(forms.Form):

	course_registered = forms.ModelChoiceField(label = 'Selected Module', queryset=Module.objects.all().order_by('name'))
	f_name = forms.CharField(label = 'First Name', max_length=20)
	l_name = forms.CharField(label = 'Last Name', max_length=20)
	email = forms.EmailField(label = 'Email Address')
	contact_number = forms.CharField(label = 'Contact', max_length=10, required=False)
	best_suited_time = forms.TimeField(widget=time_widget, help_text='ex: 10:30AM', input_formats=valid_time_formats, label = 'Preferred Time', required=False)
	comment = forms.CharField (label = 'Extra information', widget=forms.Textarea, required=False)