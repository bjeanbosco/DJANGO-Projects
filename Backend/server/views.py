from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializer import serializedStudent

# Create your views here.
@api_view(['GET','POST'])
def StudentApi(request):
    if request.method == 'GET':
     students = Student.objects.all()
     api = serializedStudent(students, many = True)
     return JsonResponse(api.data,safe= False)
    
    elif request.method == 'POST':
         api = serializedStudent(data= request.data,)
         if api.is_valid():
             api.save()
             return Response(api.data, status = status.HTTP_201_CREATED)
         
@api_view(['GET','PUT','DELETE'])
def students(request,id):
    try:
         student = Student.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        api = serializedStudent(student)
        return Response(api.data)
    elif request.method == 'PUT':
        api = serializedStudent(student , data= request.data)
        if api.is_valid():
            api.save()
            return Response(api.data)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)