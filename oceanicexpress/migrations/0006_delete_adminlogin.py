# Generated by Django 4.1.6 on 2023-05-24 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oceanicexpress', '0005_rename_login_logincred_rename_signup_signupcred'),
    ]

    operations = [
        migrations.DeleteModel(
            name='adminlogin',
        ),
    ]
