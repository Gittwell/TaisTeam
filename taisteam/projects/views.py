from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin
from projects.models import Notice, Project, Stages, LettersTais, LettersTeks, Team, LettersTechBureau, IncomingLetters

from projects.forms import AddLettersTais

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



class Index(TemplateView):
    template_name = 'projects/index.html'
    extra_context = data


class ProjectsView(ListView):

    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'table': Stages.objects.all(),
        'cat_selected': 0,
    }


class LettersTaisView(FormMixin, ListView):
    model = LettersTais
    form_class = AddLettersTais
    template_name = 'projects/letters_tais.html'
    context_object_name = 'posts'


class LettersTeksView( ListView):
    model = LettersTeks

    template_name = 'projects/letters_teks.html'
    context_object_name = 'posts'


class LettersTechBureauView(ListView):
    model = LettersTechBureau
    template_name = 'projects/letters_tech_bureau.html'
    context_object_name = 'posts'


class IncomingLettersView(ListView):
    model = IncomingLetters
    template_name = 'projects/incoming_letters.html'
    context_object_name = 'posts'


class NoticeView(ListView):
    model = Notice
    template_name = 'projects/notice.html'
    context_object_name = 'posts'


class TeamView(ListView):
    model = Team
    template_name = 'projects/team.html'
    context_object_name = 'posts'

def test(request):
    # if request.method == 'POST':
    #     form = AddLettersTais(request.POST)
    # if form.is_valid():
    #     print(form.cleande.data)
    # else:
    form = AddLettersTais()
    return render(request, 'projects/test.html', {'title': 'Главная страница', 'form': form})
