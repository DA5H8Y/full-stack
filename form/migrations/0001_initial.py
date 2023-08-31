# Generated by Django 3.0.1 on 2020-02-15 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Name must be greater than 1 character')])),
                ('breed', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
