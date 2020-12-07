# Generated by Django 3.1.4 on 2020-12-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubt', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=13)),
                ('std', models.CharField(max_length=4)),
                ('subject', models.CharField(max_length=40)),
            ],
        ),
    ]