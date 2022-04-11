from django.shortcuts import render, redirect
from .models import *
from .forms import EmployeeForm
from .filters import ExpensesFilter


# Create your views here.

def dashboard(request):
    return render(request, 'store/mainDashboard.html')


def Kassa(request):
    get_KassaInfo = Expenses.objects.all()

    myFilter=ExpensesFilter(request.GET,)

    context = {'get': get_KassaInfo, 'myFilter':myFilter}
    return render(request, 'store/Kassa.html', context)


def add(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kassa/')

    context = {'form': form}
    return render(request, 'store/addElement.html', context)


def edit(request, pk):
    project = Expenses.objects.get(id=pk)
    form = EmployeeForm(instance=project)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/kassa/')
    context = {'form': form}
    return render(request, 'store/edit.html', context)


def delete(request, pk):
    project=Expenses.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('/kassa/')
    return render(request, 'store/delete.html')
