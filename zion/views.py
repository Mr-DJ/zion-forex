from django.shortcuts import render
from zion.models import Currency
from rest_framework.response import Response
from rest_framework.decorators import api_view
from zion.serializer import CurrencySerializer

# Create your views here.
@api_view(['GET'])
def currency_list(request):
    currency = Currency.objects.all()
    serializer = CurrencySerializer(currency,many = True)
    return Response(serializer.data)