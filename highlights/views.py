from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Search
from .forms import SearchCreateForm

class IndexView(generic.CreateView):
    template_name = 'highlights/index.html'
    success_url = reverse_lazy('highlights:results')
    form_class = SearchCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(IndexView, self).form_valid(form)

class ResultsView(generic.ListView):
    template_name = 'highlights/results.html'
    fields = ('player_name', 'team_name', 'coach_name', 'game_date',
    'player_age', 'position', 'city', 'highlight_type')
    context_object_name = 'highlight_fields'

    def get_queryset(self):
        """
        Return all goals for the user
        """
        return Search.objects.last()