# Generated by Django 5.0.4 on 2024-05-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agora', '0020_alter_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateTime',
            field=models.TextField(max_length=75, null=True),
        ),
    ]
