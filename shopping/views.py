from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .operations_shopping import CREATE_SHOPPING

@api_view(['POST'])
def CREATE_SHOPPINGS(request):
	data = request.data
	result = CREATE_SHOPPING(data).Create_Shopping()
	return Response(result)

@api_view(['POST'])
def CHECK_INVOICE_NUMBER(request):
	data = request.data
	result = CREATE_SHOPPING(data).CHECK_INVOICE_NUMBER()
	return Response({'result':result})