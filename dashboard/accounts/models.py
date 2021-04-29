from django.db import models


# Create your models here.
class Expense(models.Model):
    PAYMENT = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    )

    name = models.CharField(max_length=200)
    amount = models.FloatField(null=True)
    Tenure_date = models.DateTimeField(auto_now_add=True)
    mode_of_payment = models.CharField(max_length=200, null=True, choices=PAYMENT)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    paid_by = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Earning(models.Model):
    PAYMENT = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    )

    name = models.CharField(max_length=200)
    amount = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    mode_of_payment = models.CharField(max_length=200, null=True, choices=PAYMENT)
    remarks = models.CharField(max_length=200, null=True)
    paid_by = models.CharField(max_length=200, null=True)
    received_by = models.CharField(max_length=200, null=True)
