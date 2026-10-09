
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')

        return render(request, 'result.html', {
            'name': name,
            'color': color,
            'form_data': request.POST
        })