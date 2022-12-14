# Generated by Django 4.1.1 on 2022-10-04 12:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_homework_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='create_date',
            field=models.DateField(default=datetime.date.today, help_text='The day the teacher assigned the homework'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='subject',
            field=models.ForeignKey(blank=True, help_text='The subject of the homework', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.subject'),
        ),
    ]
