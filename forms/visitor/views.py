from django.shortcuts import render

def usernames(request):
    return render(request,'login.html')

def result(request):
    username=request.GET.get('username')
    return render(request,'login_result.html',{
        'username':username,
        'form_data':request.GET
    })
