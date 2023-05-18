# Generated by Django 3.2.8 on 2023-05-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('photo', models.URLField(blank=True, max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
