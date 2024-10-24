# Generated by Django 5.1.2 on 2024-10-23 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_studentdb_alter_feeshistory_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdb',
            name='Pin',
        ),
        migrations.RemoveField(
            model_name='studentdb',
            name='Place',
        ),
        migrations.RemoveField(
            model_name='studentdb',
            name='Post',
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit'), ('Bank Transfer', 'Bank Transfer'), ('Online Payment', 'Online Payment')], max_length=20)),
                ('fees_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Paid Partially', 'Paid Partially')], max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.studentdb')),
            ],
        ),
        migrations.DeleteModel(
            name='FeesHistory',
        ),
    ]