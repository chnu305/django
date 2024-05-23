# Generated by Django 5.0.1 on 2024-05-23 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('user_email', models.CharField(max_length=60)),
                ('user_date_registration', models.DateField()),
                ('user_count_uploads', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=60)),
                ('file_upload', models.DateField()),
                ('file_size', models.IntegerField()),
                ('author_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='variant1.accounts')),
            ],
        ),
    ]