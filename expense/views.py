from django.db.models import Sum
from django.shortcuts import render

from expense.models import Expense


def index(request):
    expenses = Expense.objects.order_by("-edited")
    totalExpenses = Expense.objects.aggregate(Sum("amount"))

    context = {
        "expenses": expenses,
        "total_expenses": totalExpenses,
    }
    return render(request, "expense/index.html", context)
