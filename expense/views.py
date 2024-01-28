import datetime

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from expense.forms import ExpenseForm
from expense.models import Expense


def index(request):
    expenses = Expense.objects.order_by("-edited")
    totalExpenses = Expense.objects.aggregate(Sum("amount"))
    
    # ! calculating last 365 days expense
    lastYear = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(added__gt=lastYear)
    yearlySum = data.aggregate(Sum("amount"))

    # ! calculating last 30 days expense
    lastMonth = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(added__gt=lastMonth)
    monthlySum = data.aggregate(Sum("amount"))

    # ! calculating last 7 days expense
    lastWeek = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(added__gt=lastWeek)
    weeklySum = data.aggregate(Sum("amount"))

    context = {
        "expenses": expenses,
        "total_expenses": f"{round(totalExpenses.get("amount__sum"), 2)}",
        "yearly_sum": f"{round(yearlySum.get("amount__sum"), 2)}",
        "monthly_sum": f"{round(monthlySum.get("amount__sum"), 2)}",
        "weekly_sum": f"{round(weeklySum.get("amount__sum"), 2)}",
    }
    return render(request, "expense/index.html", context)


def add_expense(request):
    if request.method == "POST":
        expenseForm = ExpenseForm(request.POST)
        if expenseForm.is_valid():
            expenseForm.save()
            return redirect(reverse('index'))
    expenseForm = ExpenseForm()
    return render(request, "expense/add.html", {"expense_form": expenseForm})


def edit_expense(request, expenseId):
    expense = get_object_or_404(Expense, pk=expenseId)
    if request.method == "POST":
        expenseForm = ExpenseForm(request.POST, instance=expense)
        if expenseForm.is_valid():
            expenseForm.save()
            return redirect(reverse('index'))
    expenseForm = ExpenseForm(instance=expense)
    return render(request, "expense/edit.html", {"expense_form": expenseForm})


def delete_expense(request, expenseId):
    expense = get_object_or_404(Expense, pk=expenseId)
    if request.method == "POST":
        expense.delete()
        return redirect(reverse('index'))
    return render(request, "expense/delete.html", {"expense": expense})
