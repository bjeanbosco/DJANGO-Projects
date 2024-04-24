from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializer import serializedProducts


@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        store = Products.objects.all()
        api = serializedProducts(store, many = True)
        return JsonResponse(api.data, safe = False)
    
    elif request.method == 'POST':
        storing_new = serializedProducts( data = request.data)
        if storing_new.is_valid():
            storing_new.save()
            return Response(storing_new.data, status= status.HTTP_201_CREATED)
        


@api_view(['GET','PUT','DELETE'])
def product(request,id):
    
    try:
        shop = Products.objects.get(pk = id)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        api = serializedProducts(shop)
        return Response(api.data)
    
    elif request.method == 'PUT':
        res = serializedProducts( shop , data = request.data)
        if res.is_valid():
            res.save()
            return Response({"message": "data posted successful"}, status = status.HTTP_200_OK)
    
    
    elif request.method == 'DELETE':
        shop.delete()
        return Response({"message","data deleted"}, status = status.HTTP_204_NO_CONTENT)
