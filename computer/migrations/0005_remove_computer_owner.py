# Generated by Django 3.1.4 on 2020-12-23 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0004_auto_20201223_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='owner',
        ),
    ]
