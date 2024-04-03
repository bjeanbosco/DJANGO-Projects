from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import serializedDrinks
from .models import DRINKS



@api_view(['GET','POST'])

def Drinks(request):
    if request.method == 'GET':
        drinks = DRINKS.objects.all()
        api = serializedDrinks(drinks, many = True)
        return JsonResponse(api.data, safe= False)
    
    elif request.method == 'POST':
        res = serializedDrinks(data = request.data)
        if res.is_valid():
            res.save()
            return Response(res.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET','PUT','DELETE'])
def Drink(request,id):
    try:
        result = DRINKS.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        materials = serializedDrinks(result)
        return JsonResponse(materials.data , safe= False)
    
    elif request.method == 'PUT':
        respo = serializedDrinks(result , data= request.data)
        if respo.is_valid():
            respo.save()
            return Response({"message": "data updated successful"}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        result.delete()
        return Response({"message": "data deleted"}, status=status.HTTP_204_NO_CONTENT)
