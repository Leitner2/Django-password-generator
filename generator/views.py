from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#%^&**_-+=<>:;'))
    if request.GET.get('numbers'):
        characters.extend(['1','2','3','4','5','6','7','8','9','0'])
    thePassword = ''
    for i in range(length):
        thePassword += random.choice(characters)


    return render(request,'generator/password.html', {'password':thePassword})

def about(request):
    return render(request,'generator/about.html')
