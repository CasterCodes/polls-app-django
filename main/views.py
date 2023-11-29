from django.shortcuts import get_object_or_404, render,redirect
from .models import Question, Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions_list": latest_questions_list}

    return render(request, 'main/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/detail.html', {"question": question})

def result(request, question_id):
    question_results = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question_results
    }
    return render(request, 'main/result.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didnt select a choice"
        }
        return render(request, 'main/detail.html', context=context)
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result', args=(question.id,)))
   