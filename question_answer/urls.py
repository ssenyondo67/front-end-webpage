from unicodedata import name
from django.urls import  path

from . import views as views

app_name ='question_answer'

urlpatterns = [
    path('',views.question_answer, name='question_answer'),
    path('questions/',views.questions, name='questions'),
    path('mailbox/',views.mailbox, name='mailbox'),

    
]