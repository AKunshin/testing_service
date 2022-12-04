from django.shortcuts import render, get_object_or_404
from .models import Question, Category, AnswerVariant, User

# Create your views here.
def index(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    category = question.category
    answer_variants = AnswerVariant.objects.filter(question=question_id)

    context = {
        'question': question,
        'category': category,
        'answer_variants': answer_variants,
    }
    return render(request, 'app/index.html', context)


def check_answer(request, answer_id, user_id):
    user = User.objects.get(pk=user_id)
    answer = AnswerVariant.objects.get(pk=answer_id)
    if answer.is_true:
        user.user_points += answer.points








def answer(request, riddle_id):
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Option does not exist'})
    else:
        if option.correct:
            return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5], "message": "Nice! Choose another one!"})
        else:
            return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Wrong Answer!'})