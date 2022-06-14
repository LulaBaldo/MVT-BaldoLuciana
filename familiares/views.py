from django.shortcuts import render
from .models import Familiares

# Create your views here.
def familiares(request):
    familiares = Familiares.objects.all()
    ctx = {'familiares': familiares} #POR CONVENCION SE LE PONE EL MISMO NOMBRE
    return render(request, "familiares/index.html", ctx)
    