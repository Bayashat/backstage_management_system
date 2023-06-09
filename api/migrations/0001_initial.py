# Generated by Django 3.2.18 on 2023-05-08 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Last Name')),
                ('username', models.CharField(max_length=64, verbose_name='Username')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=128, verbose_name='last_name')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.SmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], verbose_name='Gender')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Account balance')),
                ('entry_time', models.DateField(verbose_name='Entry time')),
                ('depart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
