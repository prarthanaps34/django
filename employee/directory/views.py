from django.shortcuts import render

def employees(request):
    employee_list = [
        {
            "name": "anu",
            "job_title": "software developer",
            "salary": 50000,
            "full_time": True
        },
        {
            "name": "sreya",
            "job_title": "java developer",
            "salary": 30000,
            "full_time": True
        },
        {
            "name": "sreya",
            "job_title": "python developer",
            "salary": 40000,
            "full_time": False
        }
    ]

    return render(request, "employees.html", {"employees": employee_list})
