import email
from unicodedata import name
from django import forms

class cont(forms.Form):
    name = forms.CharField(label="name" , max_length=200)
    msg = forms.CharField(label="msg" , max_length=400)

