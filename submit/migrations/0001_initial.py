# Generated by Django 4.1.5 on 2023-02-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=100)),
                ('form_email', models.CharField(max_length=100)),
                ('form_phone', models.CharField(max_length=10)),
                ('form_message', models.TextField()),
            ],
        ),
    ]
