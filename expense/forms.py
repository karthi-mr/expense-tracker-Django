from django import forms
from django.db.models import Q

from expense.models import Category, Expense


class ExpenseForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Expense
        fields = ("name", "amount", "category")

    def __init__(self, user, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(
            Q(user=user) | Q(user__id=1)
        )


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Category
        fields = ("name",)
