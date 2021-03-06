# Generated by Django 3.1.3 on 2021-10-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('c_address', models.CharField(max_length=200)),
                ('c_email', models.EmailField(max_length=100)),
                ('c_country', models.CharField(max_length=200)),
                ('c_type', models.CharField(max_length=200)),
                ('c_contact', models.IntegerField()),
                ('c_url', models.URLField()),
                ('c_logo', models.ImageField(default='null', upload_to='company_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('resume', models.FilePathField(path='user_resumes')),
            ],
        ),
    ]
