# Generated by Django 4.2.3 on 2023-07-18 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='Name',
        ),
    ]
