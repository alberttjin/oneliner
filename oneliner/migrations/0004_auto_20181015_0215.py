# Generated by Django 2.1.2 on 2018-10-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneliner', '0003_auto_20181015_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events',
            field=models.ManyToManyField(to='oneliner.Event'),
        ),
        migrations.AddField(
            model_name='user',
            name='tasks',
            field=models.ManyToManyField(to='oneliner.Task'),
        ),
    ]
