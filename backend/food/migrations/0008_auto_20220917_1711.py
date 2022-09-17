# Generated by Django 4.1.1 on 2022-09-17 16:11

from django.db import migrations
from datetime import date

def create_data(apps, schema_editor):
    apps.get_model('food', 'Ticket')(ticket_number=1, match_date=date(2023, 1, 1), seat_number='A1').save()


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20220917_1704'),
    ]

    operations = [
        migrations.RunPython(create_data)
    ]