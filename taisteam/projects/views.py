from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from projects.models import Notice

data = {'categories': [{'cat': 'Home', 'img': '#home'},
                       {'cat': 'Проекты', 'img': "#speedometer2"},
                       {'cat': 'Конструкторское бюро', 'img': "#table"},
                       {'cat': 'Производство', 'img': "#grid"},
                       {'cat': 'Работники', 'img': "#people-circle"}],
        'drop_menu': ['New project...', 'Settings', 'Profile', 'Sign out']}


notice_data = {"table":[
    {'number': '1', 'title': 'ТС-245-24', 'about': 'Корректировка ТС-6519-0ГЧ', 'date': '31.07.2024', 'surname': 'Широков'},
    {'number': '2', 'title': 'ТС-246-24', 'about': 'Выпускается вновь ТС-6519-0Э6', 'date': '31.07.2024', 'surname': 'Ермилов'},
    {'number': '3', 'title': 'ТС-247-24', 'about': 'Выпускается вновь ТС-6519-0ПС', 'date': '31.07.2024', 'surname': 'Кузнецов'},
    {'number': '#', 'title': 'Обозначение', 'about': 'О чем', 'date': 'Дата', 'surname': 'Фамилия'},
    {'number': '1', 'title': 'ТС-245-24', 'about': 'Корректировка ТС-6519-0ГЧ', 'date': '31.07.2024',
     'surname': 'Широков'},
    {'number': '2', 'title': 'ТС-246-24', 'about': 'Выпускается вновь ТС-6519-0Э6', 'date': '31.07.2024',
     'surname': 'Ермилов'},
    {'number': '3', 'title': 'ТС-247-24', 'about': 'Выпускается вновь ТС-6519-0ПС', 'date': '31.07.2024',
     'surname': 'Кузнецов'},
    {'number': '#', 'title': 'Обозначение', 'about': 'О чем', 'date': 'Дата', 'surname': 'Фамилия'},
    {'number': '1', 'title': 'ТС-245-24', 'about': 'Корректировка ТС-6519-0ГЧ', 'date': '31.07.2024',
     'surname': 'Широков'},
    {'number': '2', 'title': 'ТС-246-24', 'about': 'Выпускается вновь ТС-6519-0Э6', 'date': '31.07.2024',
     'surname': 'Ермилов'},
    {'number': '3', 'title': 'ТС-247-24', 'about': 'Выпускается вновь ТС-6519-0ПС', 'date': '31.07.2024',
     'surname': 'Кузнецов'},
    {'number': '#', 'title': 'Обозначение', 'about': 'О чем', 'date': 'Дата', 'surname': 'Фамилия'},
    {'number': '1', 'title': 'ТС-245-24', 'about': 'Корректировка ТС-6519-0ГЧ', 'date': '31.07.2024',
     'surname': 'Широков'},
    {'number': '2', 'title': 'ТС-246-24', 'about': 'Выпускается вновь ТС-6519-0Э6', 'date': '31.07.2024',
     'surname': 'Ермилов'},
    {'number': '3', 'title': 'ТС-247-24', 'about': 'Выпускается вновь ТС-6519-0ПС', 'date': '31.07.2024',
     'surname': 'Кузнецов'},
    {'number': '#', 'title': 'Обозначение', 'about': 'О чем', 'date': 'Дата', 'surname': 'Фамилия'},
    {'number': '1', 'title': 'ТС-245-24', 'about': 'Корректировка ТС-6519-0ГЧ', 'date': '31.07.2024',
     'surname': 'Широков'},
    {'number': '2', 'title': 'ТС-246-24', 'about': 'Выпускается вновь ТС-6519-0Э6', 'date': '31.07.2024',
     'surname': 'Ермилов'},
    {'number': '3', 'title': 'ТС-247-24', 'about': 'Выпускается вновь ТС-6519-0ПС', 'date': '31.07.2024',
     'surname': 'Кузнецов'},
    {'number': '#', 'title': 'Обозначение', 'about': 'О чем', 'date': 'Дата', 'surname': 'Фамилия'},
    {'number': '1', 'title': 'ТС-245-24', 'about': 'Корректировка ТС-6519-0ГЧ', 'date': '31.07.2024',
     'surname': 'Широков'},
    {'number': '2', 'title': 'ТС-246-24', 'about': 'Выпускается вновь ТС-6519-0Э6', 'date': '31.07.2024',
     'surname': 'Ермилов'},
    {'number': '3', 'title': 'ТС-247-24', 'about': 'Выпускается вновь ТС-6519-0ПС', 'date': '31.07.2024',
     'surname': 'Кузнецов'},
]
}

def index(request):
    return render(request, 'projects/index.html', data)


def letters_tais(request):
    return render(request, 'projects/letters_tais.html', notice_data)


def letters_teks(request):
    return render(request, 'projects/letters_teks.html', notice_data)


def notice(request):
    posts = Notice.objects.all()
    data = {
        'title': 'Главная страница',
        'posts': posts,
    }

    return render(request, 'projects/notice.html', context=data)


def about(request):
    return render(request, 'projects/about.html')

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")