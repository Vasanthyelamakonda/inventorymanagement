# Generated by Django 4.1.6 on 2023-03-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_delete_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('brand_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('ML', models.IntegerField()),
                ('issue_price', models.IntegerField()),
                ('MRP', models.IntegerField()),
            ],
        ),
    ]
