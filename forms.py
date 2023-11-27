from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None




class EventForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length=100)
    event_date = forms.DateField(label='Event Date')
    event_location = forms.CharField(label='Event Location', max_length=100)
    event_description = forms.CharField(label='Event Description', widget=forms.Textarea)