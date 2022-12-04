from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=100, verbose_name="Наименование категории")

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    question_name = models.CharField(max_length=200, verbose_name="Формулировка вопроса")

    def __str__(self):
        return self.question_name

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class AnswerVariant(models.Model):
    question =models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    is_true = models.BooleanField(default=None, verbose_name="Ответ верный")
    points = models.PositiveIntegerField(default=0, verbose_name="Количество баллов за ответ")

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural  = "Варианты ответа"
