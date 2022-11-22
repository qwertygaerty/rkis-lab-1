from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, UserChoice
from django.template import loader, RequestContext
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('register'))

        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        print(self.kwargs['pk'])
        print(question)

        try:
            choice = UserChoice.objects.get(user=request.user, choice__question__id=self.kwargs['pk'])
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        except UserChoice.DoesNotExist:
            return super().get(request, *args, **kwargs)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required(login_url='/auth/login/')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Вы не сделали выбор'
        })
    else:
        try:
            choice = UserChoice.objects.get(user=request.user, choice_id=selected_choice.id)
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': 'Вы уже сделали выбор'
            })
        except UserChoice.DoesNotExist:
            UserChoice.objects.create(user=request.user, choice=selected_choice)
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
