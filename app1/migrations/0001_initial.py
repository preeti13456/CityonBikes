# Generated by Django 3.0.7 on 2021-01-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Available_Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rented_Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('bike', models.CharField(max_length=20, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('otp', models.IntegerField(null=True)),
            ],
        ),
    ]
