import datetime

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from expense.forms import CategoryForm, ExpenseForm
from expense.models import Category, Expense


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

    # ! calculating past 30 days sum expenses
    dailySum = (
        Expense.objects.filter(added__gt=lastMonth)
        .values('added')
        .order_by('-added')
        .annotate(sum=Sum('amount'))
    )

    # ! calculating categorical sum expenses
    categoricalSum = (
        Expense.objects.all()
        .values('category__name')
        .order_by('category')
        .annotate(sum=Sum('amount'))
    )

    context = {
        "expenses": expenses,
        "total_expenses": totalExpenses.get("amount__sum"),
        "yearly_sum": yearlySum.get("amount__sum"),
        "monthly_sum": monthlySum.get("amount__sum"),
        "weekly_sum": weeklySum.get("amount__sum"),
        "daily_sums": dailySum,
        "category_sums": categoricalSum,
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


def category_index(request):
    categories = Category.objects.all()
    return render(request, "expense/category-index.html", {"categories": categories})


def add_category(request):
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect(reverse('category-index'))
    categoryForm = CategoryForm()
    return render(request, "expense/category-add.html", {"category_form": categoryForm})


def edit_category(request, categoryId):
    category = get_object_or_404(Category, pk=categoryId)
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST, instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect(reverse('category-index'))
    categoryForm = CategoryForm(instance=category)
    return render(
        request, "expense/category-edit.html", {"category_form": categoryForm}
    )


def delete_category(request, categoryId):
    category = get_object_or_404(Category, pk=categoryId)
    if request.method == "POST":
        category.delete()
        return redirect(reverse('category-index'))
    return render(request, "expense/category-delete.html", {"category": category})
