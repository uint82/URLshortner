from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'url_shortner/index.html')
