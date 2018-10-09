from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    email = forms.EmailField()
    host = forms.CharField()
    port = forms.CharField()
    mobile = forms.CharField()