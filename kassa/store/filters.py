import django_filters
from .models import *
from django import forms


class ExpensesFilter(django_filters.FilterSet):

    class Meta:
        model = Expenses
        fields = ('typee',)
