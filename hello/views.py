from django.shortcuts import render
from django.http import JsonResponse, HttpResponse



def Hello(request):
    return HttpResponse({'Message':'Hello World!'})
# Create your views here.
