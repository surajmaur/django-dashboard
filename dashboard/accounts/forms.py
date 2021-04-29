from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Expense, Earning

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'mode_of_payment', 'remarks', 'paid_by')



class EarningForm(ModelForm):
    class Meta:
        model = Earning
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
