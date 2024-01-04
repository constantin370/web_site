from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'main_application/index.html'
    return render(request, template)