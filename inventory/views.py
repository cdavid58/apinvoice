from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import Category, SubCategory,Inventory
from .query_inventory import Query_Inventory
from company.models import Company



@api_view(['POST'])
def CREATE_INVENTORY(request):
	data = request.data
	try:
		inventory = Inventory.objects.get(code = data['code'],company = Company.objects.get(pk = data['company']))
		result = False
	except Inventory.DoesNotExist as e:
		inventory = None
		
	if inventory is None:
		q = Query_Inventory()
		q.Create_Inventory(data)
		result = True
		del q
	return Response({'Result':result})

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
	q = Query_Inventory()
	return Response(q.GET_PRODUCT(request.data))


@api_view(['POST'])
def GET_LIST_INVENTORY(request):
	data = request.data
	q = Query_Inventory()
	return Response(q.GET_LIST_INVENTORY(data))


@api_view(['POST'])
def UPDATE_PRODUCT(request):
	data = request.data
	q = Query_Inventory()
	result = q.UPDATED_PRODUCT(data)
	del q
	return Response(result)

@api_view(['POST'])
def DELETE_PRODUCT(request):
	data = request.data
	q = Query_Inventory()
	result = q.DELETE_PRODUCT(data)
	del q
	return Response({'result':result})