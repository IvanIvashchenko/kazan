from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from kazan.models import Owner


class RegistrationForm(ModelForm):

    username = forms.CharField(label=('User Name'))
    email = forms.EmailField(label=('Email Address'))
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput(render_value=False), required=True)
    password1 = forms.CharField(label=('Verify Password'), widget=forms.PasswordInput(render_value=False), required=True)

    class Meta:
        model = Owner
        exclude = ('user', 'image')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already exist, please select another')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password != password1:
            raise forms.ValidationError('The passwords did not match.  Please try again.')
        return password

class LoginForm(forms.Form):
    username = forms.CharField(label=('User Name'))
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput(render_value=False))



class CreateAdForm(forms.Form):

    title = forms.CharField(max_length=50)
    text = forms.TextInput()
    price = forms.FloatField()
