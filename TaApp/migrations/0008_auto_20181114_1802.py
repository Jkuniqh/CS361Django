# Generated by Django 2.1.2 on 2018-11-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaApp', '0007_auto_20181114_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='office_hours',
            field=models.ManyToManyField(to='TaApp.OfficeHour'),
        ),
    ]
