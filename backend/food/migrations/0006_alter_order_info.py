# Generated by Django 4.1.1 on 2022-09-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_rename_date_order_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='info',
            field=models.CharField(default='', max_length=128),
        ),
    ]