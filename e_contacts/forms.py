from django import forms
from .models import Contacts

class AddContact(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField( max_length=254, required=True)

    class Meta:
        model = Contacts
        fields = ('name', 'email')