from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Anu", "grade": "A", "passed": True},
        {"name": "Rahul", "grade": "B", "passed": True},
        {"name": "Meera", "grade": "C", "passed": False},
        {"name": "Arun", "grade": "A", "passed": True},
    ]

    return render(request, "students.html", {"students": students})