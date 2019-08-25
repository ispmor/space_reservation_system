# Generated by Django 2.2 on 2019-08-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.CharField(max_length=450)),
            ],
        ),
    ]