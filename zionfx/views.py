from locale import currency
from django.shortcuts import render
import requests;
# Create your views here.

def home(request):
    #fix
    base_url = request.build_absolute_uri('/') 
    api_url = base_url + 'currency/list/'
    currencyData = requests.get(api_url).json()
    # print(request.build_absolute_uri)
    return render(request, 'index.html', { 'currencyData': currencyData })