# Generated by Django 4.1 on 2022-10-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_alter_link_title_alter_studentlink_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('summary', models.TextField()),
                ('url', models.URLField()),
                ('display', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ize medija',
                'verbose_name_plural': 'Iz medija',
            },
        ),
    ]