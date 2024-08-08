from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

data = {'categories': [{'cat': 'Home', 'img': '#home'},
                       {'cat': 'Проекты', 'img': "#speedometer2"},
                       {'cat': 'Конструкторское бюро', 'img': "#table"},
                       {'cat': 'Производство', 'img': "#grid"},
                       {'cat': 'Работники', 'img': "#people-circle"}],
        'drop_menu': ['New project...', 'Settings', 'Profile', 'Sign out']}

def index(request):
    return render(request, 'projects/index.html', data)

def about(request):
    return render(request, 'projects/about.html')
def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")