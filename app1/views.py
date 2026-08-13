from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def funnynicio(request):
    return HttpResponse("<h1>Weeeeeiiiii =3=<h1>")
