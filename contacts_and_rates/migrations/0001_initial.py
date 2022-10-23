# Generated by Django 4.1 on 2022-10-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kontakti i informacije',
                'verbose_name_plural': 'Kontakti i informacije',
            },
        ),
        migrations.CreateModel(
            name='RateList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratelist_pdf', models.FileField(upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cjenik',
                'verbose_name_plural': 'Cjenici',
            },
        ),
    ]
