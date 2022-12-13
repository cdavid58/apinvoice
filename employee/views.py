from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import Employee
from company.models import Company

@api_view(['POST'])
def Register_Employee(request):
	data = request.data
	employee = Employee.objects.get(documentI = data['documentI'])
	employee.Block_Employee()
	Employee(
		documentI = data['documentI'],
		name = data['name'],
		phone = data['phone'],
		email = data['email'],
		user = data['user'],
		psswd = data['psswd'],
		company = Company.objects.get(nit = data['company'])
	).save()
	return Response({'Result':True})

@api_view(['POST'])
def Validate_Login(request):
	data = request.data
	try:
		employee = Employee.objects.get(user = data['user'], psswd=data['psswd'])
		result = True
	except Employee.DoesNotExist:
		result = False
	return Response({'Result':result})
