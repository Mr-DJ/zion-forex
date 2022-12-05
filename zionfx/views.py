from locale import currency
from django.shortcuts import render
import requests;
# Create your views here.

def home(request):
    currencyData = requests.get('http://127.0.0.1:8000/currency/list/').json()
    return render(request, 'index.html', { 'currencyData': currencyData })