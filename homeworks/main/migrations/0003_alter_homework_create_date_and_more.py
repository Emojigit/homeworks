# Generated by Django 4.1.1 on 2022-10-04 12:53

import datetime
from django.db import migrations, models
import django_enum.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_subject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='create_date',
            field=models.DateField(default=datetime.date.today, help_text='The day the teacher assigned the homeworkA'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='description',
            field=models.CharField(help_text='The content of the homework, including instructions from the teacher.', max_length=50),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateField(help_text='The day students should hand in their homework'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='type',
            field=django_enum.fields.EnumCharField(choices=[('hw', 'Homeworks'), ('nt', 'Notifications'), ('al', 'Alert')], default='hw', help_text='Type of the homework\nHomework: A regular homework\nNotify: Not a homework, but something teachers told students to do\nAlert: Something quite urgent', max_length=2),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(help_text='The name of the subject', max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='short_code',
            field=models.CharField(help_text='A abbreviation of the subject name', max_length=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sort_key',
            field=models.CharField(help_text='A string, usually integers, to help sort the list of homeworks.', max_length=10),
        ),
    ]