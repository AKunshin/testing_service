from django.shortcuts import render
from .models import Question, Category, AnswerVariant

# Create your views here.
def index(request, question_id):
    question = Question.objects.get(pk=question_id)
    category = question.category
    answer_variants = AnswerVariant.objects.filter(question=question_id)

    context = {
        'question': question,
        'category': category,
        'answer_variants': answer_variants,
    }
    return render(request, 'app/index.html', context)