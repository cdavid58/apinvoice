from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .query_client import Create_Client

c = Create_Client()

@api_view(['POST'])
def CREATE_CLIENT(request):
	data = request.data
	result = c.CREATE_CLIENT(data)
	return Response({'Result':result})

@api_view(['POST'])
def GET_LIST_CLIENT(request):
	data = request.data
	return Response({'client':c.GET_LIST_CLIENT(data)})

@api_view(['POST'])
def GET_CLIENT(request):
	data = request.data
	return Response({'client':c.GET_CLIENT(data)})

@api_view(['POST'])
def DELETE_CLIENT(request):
	data = request.data
	return Response({'client':c.DELETE_CLIENT(data)})

@api_view(['POST'])
def EDIT_CLIENT(request):
	data = request.data
	return Response({'result':c.EDIT_CLIENT(data)})