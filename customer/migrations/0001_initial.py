# Generated by Django 4.0.1 on 2022-01-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_fname', models.CharField(max_length=25)),
                ('customer_lname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('confirm_password', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
