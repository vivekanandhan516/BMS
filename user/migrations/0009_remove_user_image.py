# Generated by Django 4.0.6 on 2022-10-14 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_delete_userregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
