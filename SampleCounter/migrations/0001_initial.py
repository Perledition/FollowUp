# Generated by Django 2.1.5 on 2019-03-29 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('active_since', models.DateField(default=datetime.datetime(2019, 3, 29, 20, 5, 29, 801701))),
            ],
        ),
        migrations.CreateModel(
            name='PostEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
