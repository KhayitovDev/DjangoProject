from django import forms
from .models import Expenses


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('typee', 'byWho', 'amount', 'valuta','Kurs','summa', 'category', 'izoh')
        widgets = {
            'typee': forms.TextInput(attrs={'class': 'form-control'}),
            'byWho': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'valuta': forms.TextInput(attrs={'class': 'form-control'}),
            'Kurs': forms.TextInput(attrs={'class': 'form-control'}),
            'summa': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'izoh': forms.TextInput(attrs={'class': 'form-control'}),

        }
