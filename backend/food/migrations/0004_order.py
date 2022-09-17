# Generated by Django 4.1.1 on 2022-09-17 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('choices', models.ManyToManyField(to='food.option')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.ticket')),
            ],
        ),
    ]