# Generated by Django 2.2 on 2019-08-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('equipement', models.TextField(help_text='Enter a brief description of the room', max_length=1000)),
                ('capacity', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('i', 'In Use'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Room availability', max_length=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
