from django import forms

class CreateAdForm(forms.Form):

    title = forms.CharField(max_length=50)
    text = forms.TextInput()
    price = forms.FloatField()
