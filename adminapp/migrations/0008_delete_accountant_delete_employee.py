# Generated by Django 4.1.6 on 2023-04-29 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_accountant_employee_alter_brand_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accountant',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
