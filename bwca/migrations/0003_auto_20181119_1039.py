# Generated by Django 2.1.3 on 2018-11-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwca', '0002_auto_20181119_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camper',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='camper',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
