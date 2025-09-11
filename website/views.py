from django.shortcuts import render

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def content_view(request):
    return render(request, 'website/contact.html')

def elements_view(request):
    return render(request, 'website/elements.html')