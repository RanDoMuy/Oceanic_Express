# Generated by Django 4.1.6 on 2023-05-17 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oceanicexpress', '0002_logins_rename_user_signups_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='logins',
            new_name='login',
        ),
        migrations.RenameModel(
            old_name='signups',
            new_name='signup',
        ),
    ]
