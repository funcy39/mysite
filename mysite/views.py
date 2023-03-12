from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def raise_500(request):
#     raise HttpResponseServerError
