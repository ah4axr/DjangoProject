from django.template import loader
from django.http import Http404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'highlights/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'highlights/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.ListView):
    template_name = 'highlights/results.html'
    context_object_name = 'highlights_list'

    def get_queryset(self):
        """
        Return all goals for the user
        """
        return Question.objects.filter(pub_date__lte=timezone.now())