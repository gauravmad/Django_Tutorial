# Generated by Django 4.1.5 on 2023-02-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_employ'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=50)),
                ('service_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
