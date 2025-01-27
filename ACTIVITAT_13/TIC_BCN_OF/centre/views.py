from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def students(request):
    students = [
        {"id": 1, "nom": "Oriol", "cognom": "Farssac", "edat": 20, "curs": "DAM2B"},
        {"id": 2, "nom": "Anna", "cognom": "López", "edat": 19, "curs": "DAW2A"},
        {"id": 3, "nom": "Marc", "cognom": "García", "edat": 21, "curs": "DAW2B"},
        {"id": 4, "nom": "Laura", "cognom": "Martínez", "edat": 22, "curs": "DAW1A"},
    ]
    return render(request, 'index_students.html', {'students': students})

def teachers(request):
    teachers = [
        {"id": 1, "nom": "Oriol", "cognom": "Farssac", "edat": 20, "rol": "teacher", "curs": "DAM2B, DAW2A"},
        {"id": 2, "nom": "Roger", "cognom": "Sobrino", "edat": 39, "rol": "teacher", "curs": "DAM2B, DAW2A"},
        {"id": 3, "nom": "Josep Oriol", "cognom": "Roca", "edat": 25, "rol": "teacher", "curs": "DAW2B, DAW2A, DAW1A"},
        {"id": 4, "nom": "Juanma", "cognom": "Biel", "edat": 24, "rol": "teacher", "curs": "DAW2B, DAW2A"}
    ]
    return render(request, 'index_teachers.html', {'teachers': teachers})
