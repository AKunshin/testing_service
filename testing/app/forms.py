from .models import Category, Question, AnswerVariant
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category','question_name']
