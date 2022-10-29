# Generated by Django 4.0.6 on 2022-10-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_account_remove_user_emply_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aadhar',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='user',
            name='emply_num',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%D'),
        ),
    ]