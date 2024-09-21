# Generated by Django 4.1.13 on 2024-09-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeptHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('prn', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('year', models.CharField(choices=[('2nd', 'SY'), ('3rd', 'TY'), ('4th', 'B.Tech')], max_length=10)),
                ('department', models.CharField(choices=[('Computer', 'Computer'), ('IT', 'IT'), ('Mechanical', 'Mechanical')], max_length=50)),
                ('roll_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=15)),
            ],
        ),
    ]
