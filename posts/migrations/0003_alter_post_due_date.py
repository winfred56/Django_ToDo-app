# Generated by Django 3.2.9 on 2021-11-01 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211101_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
