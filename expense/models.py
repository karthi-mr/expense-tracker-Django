from django.db import models


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    added = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    class Meta:
        db_table = "expense_db"

    def __str__(self):
        return self.name
