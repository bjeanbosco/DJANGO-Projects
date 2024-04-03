#from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import serializerStudent

@api_view(['GET','POST'])
def students(request):
    if request.method  == 'GET':
        school = Student.objects.all()
        api = serializerStudent(school, many = True)
        return JsonResponse(api.data, safe= False)
    elif request.method == 'POST':
        school = serializerStudent(data= request.data)
        if school.is_valid():
            school.save()
            return Response(school.data, status=status.HTTP_201_CREATED)
        return Response({'message': "bad response"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def student(request,id):
    try:
        studenter = Student.objects.get(pk = id)
    except:
        return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        api = serializerStudent(studenter)
        return JsonResponse(api.data , safe= False)
    
    elif request.method == 'PUT':
        stud = serializerStudent(studenter , data= request.data)
        if stud.is_valid():
            stud.save()
            return Response(stud.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        studenter.delete()
        return Response({'message': "data deleted"}, status=status.HTTP_204_NO_CONTENT)