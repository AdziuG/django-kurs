from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'films': wszystkie})



