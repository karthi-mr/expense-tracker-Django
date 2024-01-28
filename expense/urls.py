from django.urls import path

from expense import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add-expense'),
    path('edit/<int:expenseId>', views.edit_expense, name='edit-expense'),
    path('delete/<int:expenseId>', views.delete_expense, name='delete-expense'),
]
