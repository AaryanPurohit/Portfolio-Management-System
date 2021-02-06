# Generated by Django 3.1.3 on 2021-02-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_stockholding_buying_values'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockholding',
            name='buying_values',
        ),
        migrations.AddField(
            model_name='stockholding',
            name='buying_value',
            field=models.JSONField(default={}),
        ),
    ]
