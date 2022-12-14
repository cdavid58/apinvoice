# Generated by Django 3.2.8 on 2022-12-15 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('employee', '0003_remove_employee_count_intent_block'),
        ('pos', '0002_alter_invoice_pos_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet_POS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelled', models.BooleanField(default=False)),
                ('days_in_debt', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.invoice_pos')),
            ],
        ),
    ]
