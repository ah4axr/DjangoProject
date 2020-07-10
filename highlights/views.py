from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db import connection

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
    fields = ('player_lname',
    'player_position', 'highlight_type')
    context_object_name = 'highlight_fields'

    def get_queryset(self):
        plname = Search.objects.last().player_lname
        pposition = Search.objects.last().player_position
        htype = Search.objects.last().highlight_type

        with connection.cursor() as cursor:
            cursor.execute('''SELECT VIDEO_PATH 
            FROM VIDEO, HIGHLIGHT, PLAYER 
            WHERE VIDEO.HIGHLIGHT_ID = HIGHLIGHT.HIGHLIGHT_ID 
            AND PLAYER_LNAME = %s
            AND PLAYER.PLAYER_POSITION = %s 
            AND PLAYER.PLAYER_ID = HIGHLIGHT.PLAYER_ID 
            AND HIGHLIGHT.HIGHLIGHT_TYPE = %s
            GROUP BY VIDEO_PATH
            ''', 
            [plname, pposition, htype])
            row = cursor.fetchall()
        print(row)
        
        return row