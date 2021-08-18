from re import M
from django.shortcuts import render
from .models import Question, Quizzes
from .serializers import QuizSerializer
from rest_framework.views import APIView

from rest_framework import generics
# Create your views here.
class Quiz(generics.ListAPIView):
    
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format:None, *args, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
