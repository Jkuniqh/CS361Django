# Generated by Django 2.1.2 on 2018-11-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaApp', '0002_auto_20181109_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='defaultpass', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=10),
        ),
    ]