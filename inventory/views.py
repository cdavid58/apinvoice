from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import Category, SubCategory
from .query_inventory import Query_Inventory

q = Query_Inventory()

@api_view(['POST'])
def CREATE_INVENTORY(request):
	data = request.data
	q.Create_Inventory(data)
	return Response({'Result':True})

@api_view(['POST'])
def Create_Category(request):
	data = request.data
	Category(
		name = str(data['name'])
	).save()
	return Response({'Result':data})

@api_view(['POST'])
def CreateSubCategories(request):
	data = request.data
	SubCategory(
		name =str(data['name']),
		category = Category.objects.get(pk = data["id_category"])
	).save()
	return Response({'Result':data})

@api_view(['POST'])
def GET_PRODUCT(request):
	return Response(q.GET_PRODUCT(request.data))


@api_view(['POST'])
def GET_LIST_INVENTORY(request):
	data = request.data
	return Response(q.GET_LIST_INVENTORY(data))