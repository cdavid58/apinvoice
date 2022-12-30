from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .query_api import Query_Company


@api_view(['POST'])
def Create_Company(request):
	# print(str(request.headers['Authorization']).replace('Bearer','').strip())
	register = Query_Company(request.data)
	result = False
	if register.Create_Company():
		result = True
		if register.Create_License():
			result = True
		else:
			result = False 
	return Response({'Result':result})	


