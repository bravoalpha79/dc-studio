# Generated by Django 4.1 on 2022-09-25 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='name',
            new_name='name_and_title',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='title',
        ),
    ]
