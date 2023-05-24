# Generated by Django 4.1.6 on 2023-05-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanicexpress', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('Password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
        migrations.RenameModel(
            old_name='user',
            new_name='signups',
        ),
        migrations.AlterField(
            model_name='package',
            name='Current_Location',
            field=models.CharField(max_length=50, verbose_name='Current Package Location'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Dispatch_Location',
            field=models.CharField(max_length=50, verbose_name='Dispatch Location'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Package_Description',
            field=models.CharField(max_length=50, verbose_name='Package Description'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Receiver_Contact',
            field=models.CharField(max_length=11, verbose_name='Receiver Contact'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Sender_Contact',
            field=models.CharField(max_length=11, verbose_name='Sender Contact'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Shipment_Destination',
            field=models.CharField(max_length=50, verbose_name='Shipment Destination'),
        ),
    ]
