from django import forms

class AddressForm(forms.Form):
    address = forms.CharField()
    distance = forms.CharField(initial=25)
