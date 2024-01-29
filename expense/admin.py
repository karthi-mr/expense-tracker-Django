from django.contrib import admin

from expense.models import Category, Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "category", "edited", "added")
    list_display_links = ("name",)
    readonly_fields = ("added", "edited")
    list_editable = ("amount",)
    ordering = ("-added",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    ordering = ("name",)
