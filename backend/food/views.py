from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Ticket, Option, Order
from .serializers import OptionSerializer

@api_view(['GET'])
def option_list(request):
    if request.method == 'GET':
        data = Option.objects.all()

        serializer = OptionSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)