from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from kazan.models import Owner


class RegistrationForm(ModelForm):

    username = forms.CharField(label=('User Name'))
    email = forms.EmailField(label=('Email Address'))
    passwd = forms.CharField(label=('Password'), widget=forms.PasswordInput(render_value=False), required=True)
    checked_passwd = forms.CharField(label=('Verify Password'), widget=forms.PasswordInput(render_value=False), required=True)
    image = forms.ImageField(label=('User Picture'), required=False)


    class Meta:
        model = Owner
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already exist, please select another')

    def clean_password(self):
        password = self.cleaned_data.get('passwd')
        checked_password = self.cleaned_data.get('checked_passwd')
        if password != checked_password:
            raise forms.ValidationError('The passwords did not match.  Please try again.')
        return password

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label=('User Name'))
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput(render_value=False))

class CreateAdForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    image = forms.ImageField()
