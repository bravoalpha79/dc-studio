# Generated by Django 4.1 on 2022-10-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educational_pages', '0005_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='date_published',
        ),
    ]