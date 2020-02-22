from django.shortcuts import render

def home(request):
    return render(request, 'excuseTypes/home.html')

def emergency(request):
    return render(request, 'excuseTypes/emergency.html')

def scheduled(request):
    return render(request, 'excuseTypes/scheduled.html')
