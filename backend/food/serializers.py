from rest_framework import serializers
from .models import Ticket, Option, Order

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['pk', 'ticket_number', 'match_date', 'seat_number']

class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['pk', 'name', 'price']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['pk', 'order_date', 'info', 'ticket', 'choices']