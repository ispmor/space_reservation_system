# Generated by Django 2.2.1 on 2019-06-30 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0011_auto_20190527_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]