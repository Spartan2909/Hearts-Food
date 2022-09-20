from django.db import models

class Ticket(models.Model):
    ticket_number = models.IntegerField()
    match_date = models.DateField()
    seat_number = models.CharField(max_length=16)

class Option(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    option_type = models.CharField(max_length=2, choices=[
        ('ME', 'Meal'),
        ('SN', 'Snack'),
        ('DR', 'Drink'),
        ('SI', 'Side')
    ])

class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    info = models.CharField(max_length=128, default='')
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE
    )
    choices = models.ManyToManyField(
        Option
    )