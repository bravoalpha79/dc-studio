# Generated by Django 4.1 on 2022-10-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='studentlink',
            name='title',
            field=models.CharField(default='', max_length=254, null=True),
        ),
    ]
