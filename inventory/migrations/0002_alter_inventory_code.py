# Generated by Django 3.2.8 on 2023-01-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='code',
            field=models.CharField(max_length=100),
        ),
    ]
