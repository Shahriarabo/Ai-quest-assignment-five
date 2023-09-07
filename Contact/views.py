from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse('<h1>My Name is Abdullah Al Shahriar</h1>')