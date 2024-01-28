# Generated by Django 5.0.1 on 2024-01-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=50)),
                ('added', models.DateField(auto_now_add=True)),
                ('edited', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'expense_db',
            },
        ),
    ]