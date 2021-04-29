from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reg/', views.reg, name="reg"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('add/', views.addpage, name="add"),
    path('update_expense/<Expense_id>/', views.updateExpense, name="update_Expense"),
    path('expense_delete/<Expense_id>/', views.DeleteExpense, name="delete_Expense"),
    path('addearn/', views.addearnpage, name="addearn"),
    path('update_earn/<Earning_id>/', views.updateEarn, name="update_Earning"),
    path('earning_delete/<Earning_id>/', views.DeleteEarn, name="delete_Earn"),
]
