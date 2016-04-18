from django.shortcuts import render

from django.http import HttpResponse


def input(request):
    return render(request, 'coding/input.html')

def sub(request):
    return render(request, 'coding/sub.html')
