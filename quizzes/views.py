from django.shortcuts import render
from django.http import JsonResponse
from .models import Quiz
from .serializers import QuizSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status

@api_view(['POST'])
def quiz_create(request):
    serializer =  QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_active_quiz(request):
    try:
        quizzes = Quiz.objects.filter(status="active")
        serialized_quizzes = QuizSerializer(quizzes, many=True).data
        for quiz in serialized_quizzes:
            quiz.pop('right_answer')
        return JsonResponse(serialized_quizzes, safe=False)
    except Quiz.DoesNotExist:
        return JsonResponse({"error": "No actice quizzes"}, status=404)

@api_view(['GET'])
def get_result(request, quiz_id):
    try:
        quiz = Quiz.objects.get(id=quiz_id)
        result = {"id": quiz.id, "right_answer": quiz.right_answer}
        return JsonResponse(result)
    except Quiz.DoesNotExist:
        return JsonResponse({"error": "Quiz does not exist"}, status=404)



@api_view(['GET'])
def quiz_list(request):
    quiz = Quiz.objects.all()
    serializer = QuizSerializer(quiz , many=True )
    for quiz in serializer.data:
        quiz.pop('right_answer')
    return JsonResponse(serializer.data , safe=False)
    



