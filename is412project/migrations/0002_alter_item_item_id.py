# Generated by Django 3.2.9 on 2021-12-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is412project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default=0),
        ),
    ]