# Generated by Django 2.0.1 on 2020-01-06 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_view', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='title',
        ),
    ]