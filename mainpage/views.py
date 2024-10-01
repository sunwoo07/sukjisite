from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage/mainpage.html')

def privacypolicy(request):
    return render(request, 'mainpage/privacy_policy.html')