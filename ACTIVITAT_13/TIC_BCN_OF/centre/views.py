from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def students(request):
    student = {"nom": "Oriol", "cognom": "Farssac", "edat": 20}
    return render(request, 'index.html', {'students': student})

def teachers(request):
    teacher = {"nom": "Oriol", "cognom": "Farssac", "edat": 20}
    return render(request, 'index.html', {'teachers': teacher})
