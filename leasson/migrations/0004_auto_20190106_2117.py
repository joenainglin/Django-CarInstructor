# Generated by Django 2.1.1 on 2019-01-06 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasson', '0003_lesson_datenow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='datenow',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='now',
        ),
    ]