from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%'))

    length = int(request.GET.get('length',12))

    for i in range(length):
        thepassword += random.choice(chars)


    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')