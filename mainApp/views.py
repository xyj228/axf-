from django.shortcuts import render

# Create your views here.
from mainApp.models import Wheel


def home(request):
    wheels = Wheel.objects.all()
    context = {
        'wheel': wheels
    }
    for i in wheels:
        print(i.img)
    return render(request, 'axf/main/home/home.html', context=context)


def market(request):
    return render(request, 'axf/main/market/market.html')


def cart(request):
    return render(request, 'axf/main/cart/cart.html')


def mine(request):
    return render(request, 'axf/main/mine/mine.html')
