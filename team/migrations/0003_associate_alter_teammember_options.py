# Generated by Django 4.1 on 2022-09-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_rename_name_teammember_name_and_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_title', models.CharField(max_length=254)),
                ('biography', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Suradnik',
                'verbose_name_plural': 'Suradnici',
            },
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'verbose_name': 'Član tima', 'verbose_name_plural': 'Članovi tima'},
        ),
    ]
