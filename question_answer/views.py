from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


# Create your views here.
def question_answer(request):
    content={
               "categories":[1,2,3,4,5,6,6,7,8,9,10,11,12,13,14],
               }       
    
    return render(request, 'question_answer/question_answer.html',content)

def questions(request):
    content={
               "categories":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
               }       
    
    return render(request, 'question_answer/questions.html',content)

def mailbox(request):
    content={
               "categories":[1,2,3,4,5,6,6,7,8,9,10,11,12,13,14,3,4,5,6,7,8,8,9,0,5,4,3,2,2,4,5,6,7],
               }       
    
    return render(request, 'question_answer/mailbox.html',content)
