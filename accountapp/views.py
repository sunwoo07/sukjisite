from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return HttpResponse('Helloworld')

def index(request):
    return render(request, 'base.html')