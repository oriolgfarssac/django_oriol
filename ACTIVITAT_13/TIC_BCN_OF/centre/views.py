from django.shortcuts import render
from django.http import HttpResponse

studentsArr = [
    {"id": 1, "nom": "Oriol", "cognom": "Garcia", "rol": "Estudiant", "edat": 20, "curs": "DAW"},
    {"id": 2, "nom": "Anna", "cognom": "Martínez", "rol": "Estudiant", "edat": 21, "curs": "DAW"},
    {"id": 3, "nom": "Marc", "cognom": "Pérez", "rol": "Estudiant", "edat": 22, "curs": "DAW"},
    {"id": 4, "nom": "Laura", "cognom": "Sánchez", "rol": "Estudiant", "edat": 19, "curs": "DAW"},
]

teachersArr = [
    {"id": 1, "nom": "Oriol", "cognom": "Lopez", "rol": "Professor", "edat": 35, "especialitat": "M05"},
    {"id": 2, "nom": "Roger", "cognom": "Vázquez", "rol": "Professor", "edat": 40, "especialitat": "M07"},
    {"id": 3, "nom": "Josep Oriol", "cognom": "González", "rol": "Professor", "edat": 45, "especialitat": "M06"},
    {"id": 4, "nom": "Juanma", "cognom": "Ramírez", "rol": "Professor", "edat": 38, "especialitat": "M10"},
]

def students(request):
    return render(request, 'index_students.html', {'students': studentsArr})

def student(request, pk):
    studentObj = next((s for s in studentsArr if s['id'] == int(pk)), None)
    if studentObj is None:
        return HttpResponse("Estudiant no trobat", status=404)
    return render(request, 'index_student.html', {'student': studentObj})

def teachers(request):
    return render(request, 'index_teachers.html', {'teachers': teachersArr})

def teacher(request, pk):
    teacherObj = next((t for t in teachersArr if t['id'] == int(pk)), None)
    if teacherObj is None:
        return HttpResponse("Professor no trobat", status=404)
    return render(request, 'index_teacher.html', {'teacher': teacherObj})
