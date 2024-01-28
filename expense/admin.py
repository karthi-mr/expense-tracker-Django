from django.contrib import admin

from expense.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "category", "edited")
    list_display_links = ("name",)
    readonly_fields = ("added", "edited")
    list_editable = ("amount",)
