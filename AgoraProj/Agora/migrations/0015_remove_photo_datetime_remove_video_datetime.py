# Generated by Django 5.0.4 on 2024-05-04 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agora', '0014_audience_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='dateTime',
        ),
        migrations.RemoveField(
            model_name='video',
            name='dateTime',
        ),
    ]
