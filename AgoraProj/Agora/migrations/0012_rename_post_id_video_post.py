# Generated by Django 5.0.4 on 2024-05-03 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agora', '0011_rename_post_id_photo_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='post_ID',
            new_name='post',
        ),
    ]
