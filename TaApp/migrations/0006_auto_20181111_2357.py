# Generated by Django 2.1.2 on 2018-11-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaApp', '0005_auto_20181111_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='office_hours',
            field=models.ManyToManyField(to='TaApp.OfficeHour'),
        ),
    ]
