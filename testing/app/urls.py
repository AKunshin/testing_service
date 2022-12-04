from django.urls import path
from .views import index

urlpatterns = [
    path('testing/<int:question_id>/', index, name='index'),
]