from django.shortcuts import render

def gallery(request):
    return render(request, 'gallery/gallery.html')

def contact(request):
    return render(request, 'gallery/contact.html')
