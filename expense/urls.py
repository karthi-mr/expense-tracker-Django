from django.urls import path

from expense import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add-expense'),
    path('edit/<int:expenseId>/', views.edit_expense, name='edit-expense'),
    path('delete/<int:expenseId>/', views.delete_expense, name='delete-expense'),
    path('category/', views.category_index, name='category-index'),
    path('category/add/', views.add_category, name='add-category'),
    path('category/edit/<int:categoryId>/', views.edit_category, name='edit-category'),
    path(
        'category/delete/<int:categoryId>/',
        views.delete_category,
        name='delete-category',
    ),
]
