# Generated by Django 4.0.5 on 2022-06-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='age',
            field=models.IntegerField(default=10),
        ),
    ]
