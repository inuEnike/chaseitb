from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,  SetPasswordForm, PasswordResetForm
from django.contrib.auth import get_user_model
from .models import *
from django.forms import ModelForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)



class ProfileForm (ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'name']


class DepositForm (ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user']

class CardForm (ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ['user']


class AccountnumberForm (ModelForm):
    class Meta:
        model = Accountnumber
        fields = '__all__'
        exclude = ['user']


class TransferForm (ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'
        exclude = ['user', 'name', 'status']

class WithdrawForm (ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'
        exclude = ['user', 'name', 'status']

class PinForm (ModelForm):
    class Meta:
        model = Pin
        fields = '__all__'
        exclude = ['user', 'name']
