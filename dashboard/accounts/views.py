from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ExpenseForm, EarningForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    expenses = Expense.objects.all()
    earnings = Earning.objects.all()

    context = {'expenses':expenses, 'earnings':earnings}

    return render(request, 'accounts/dashboard.html', context)



def reg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/reg.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addpage(request,):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/add.html', context)

@login_required(login_url='login')
def addearnpage(request):

    form = EarningForm()
    if request.method == 'POST':
        form = EarningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'accounts/addearn.html', context)

@login_required(login_url='login')
def updateExpense(request, Expense_id):

    item = Expense.objects.get(pk=Expense_id)
    form = ExpenseForm(instance=item)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'accounts/add.html', context)

@login_required(login_url='login')
def updateEarn(request, Earning_id):

    item = Earning.objects.get(pk=Earning_id)
    form = EarningForm(instance=item)

    if request.method == 'POST':
        form = EarningForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/addearn.html', context)

@login_required(login_url='login')
def DeleteExpense(request, Expense_id):

    item = Expense.objects.get(pk=Expense_id)
    item.delete()
    return redirect('home')

@login_required(login_url='login')
def DeleteEarn(request, Earning_id):

    item = Earning.objects.get(pk=Earning_id)
    item.delete()
    return redirect('home')
