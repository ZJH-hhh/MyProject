# Generated by Django 3.2.8 on 2023-09-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=256)),
                ('job_name', models.CharField(max_length=256)),
                ('company_name', models.CharField(max_length=256)),
                ('company_size', models.CharField(max_length=256)),
                ('company_type', models.CharField(max_length=256)),
                ('salary', models.CharField(max_length=256)),
                ('edu', models.CharField(max_length=256)),
                ('skill', models.CharField(max_length=256)),
                ('exp', models.CharField(max_length=256)),
            ],
        ),
    ]
