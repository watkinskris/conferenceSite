from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


def activities(request):
    return render(request, 'activities.html')


def meals(request):
    return render(request, 'meals.html')


def keynote(request):
    return render(request, 'keynote.html')


def nametag8(request):
    return render(request, 'nametags8gen.html')


def nametag10(request):
    return render(request, 'nametags10gen.html')