# Generated by Django 3.2.8 on 2022-12-10 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_count_intent_employee_count_intent_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='count_intent_block',
        ),
    ]
