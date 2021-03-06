# Generated by Django 3.2.9 on 2021-11-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField()),
                ('priority', models.CharField(choices=[('Important', 'Important'), ('Very Important', 'Very Important'), ('Not So Important', 'Not So Important')], default='Important', max_length=18)),
                ('done', models.BooleanField()),
            ],
        ),
    ]
