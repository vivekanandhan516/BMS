# Generated by Django 4.0.6 on 2022-10-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_accountregister_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountregister',
            name='email',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
