from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .forms import InputForm

from .models import Team, Player

class SampleTemplateViews(generic.TemplateView):
    template_name = "myapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = 'bababa'
        print(context)
        return context


class TeamList(generic.ListView):
    model = Team
    ordering = 'name'


class PlayerList(generic.ListView):
    model = Player
    ordering = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        context['team'] = self.team
        return context

    def get_queryset(self):
        team = self.team = get_object_or_404(Team, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(team=team)
        return queryset


def input(request):
    if request.method == 'POST':
        f = InputForm(request.POST)
    else:
        f = InputForm()
    return render(request, 'myapp/inputform.html', {'form1': f})

