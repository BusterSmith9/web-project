# Generated by Django 3.1.7 on 2021-03-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medhub', '0002_auto_20210308_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
