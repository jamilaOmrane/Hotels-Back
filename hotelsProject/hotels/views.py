from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hotel
from .serializers import HotelSerializer

# def home(request):
#     hotel_data = Hotel.objects.all()
#     for h in hotel_data:
#         print('Hotel Name: ', h.name)

#     return HttpResponse('This url iw working')

@api_view(['GET'])
def hotels_list(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many = True)
        return Response(serializer.data)