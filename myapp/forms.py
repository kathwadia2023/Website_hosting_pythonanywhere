from django import forms
from .models import *


class signup_form(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = '__all__'

class update_form(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = ['firstname','lastname','username','password','city','state','mobile']

class Notes_form(forms.ModelForm):
    class Meta:
        model = my_notes
        fields = "__all__"

class Feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields = "__all__"
