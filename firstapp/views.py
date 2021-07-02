from django.shortcuts import render


def check(request):
    return render(request, 'check.html')


def login(request):
    return render(request, 'login.html')
