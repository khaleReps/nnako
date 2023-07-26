from django.shortcuts import render

def home(request):
    content = {

    }
    return render(request, 'web_app/home.html', content)
