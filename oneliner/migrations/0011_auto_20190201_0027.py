# Generated by Django 2.1.5 on 2019-02-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneliner', '0010_auto_20190201_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
