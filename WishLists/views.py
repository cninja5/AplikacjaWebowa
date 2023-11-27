from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def createList(response):
    return render(response, 'createList.html')