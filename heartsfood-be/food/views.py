from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Ticket, Option, Order
from .serializers import OrderSerializer, TicketSerializer, OptionSerializer

@api_view(['GET'])
def ticket(request, ticket_number):
    try:
        data = Ticket.objects.get(ticket_number=ticket_number)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TicketSerializer(data, context={'request': request})

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def option(request):
    if request.method == 'GET':
        data = Option.objects.all()

        serializer = OptionSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def order(request):
    if request.method == 'GET':
        data = Order.objects.all()

        serializer = OrderSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)