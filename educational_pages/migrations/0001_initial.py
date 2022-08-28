# Generated by Django 4.1 on 2022-08-28 19:25

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
                ('title', models.CharField(max_length=254)),
                ('author', models.CharField(blank=True, max_length=254, null=True)),
                ('tags', models.CharField(blank=True, max_length=254, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('published', models.DateField(auto_now_add=True)),
            ],
        ),
    ]