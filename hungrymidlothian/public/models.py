from django.db import models

class User(models.Model):
    email = models.CharField(max_length=35)
    pwdHash = models.CharField('password hash', max_length=64)

class Ticket(models.Model):
    ticketNum = models.CharField(max_length=30)
    matchDate = models.DateField()
    seatNum = models.CharField(max_length=6)
    user = models.ForeignKey()