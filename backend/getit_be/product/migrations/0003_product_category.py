# Generated by Django 3.1.7 on 2021-07-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210725_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.TextField(default='Groceries', max_length=100),
        ),
    ]