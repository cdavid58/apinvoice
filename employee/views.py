from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import Employee
from company.models import Company
import base64
from PIL import Image
from io import BytesIO

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
		result = {'result':True,'company':employee.company.pk,'employee':employee.pk}
	except Employee.DoesNotExist:
		result = {'result':False}
	return Response(result)


@api_view(['POST'])
def GET_LIST_EMPLOYEE(request):
	data = request.data['company']
	_data = [
		{
			'pk':i.pk,
			'name':i.name,
			'phone':i.phone,
			'email':i.email
		}
		for i in Employee.objects.filter(company = Company.objects.get(pk = data) )
	]
	return Response(_data)

@api_view(['POST'])
def GET_EMPLOYEE(request):
	employee = Employee.objects.get(pk = request.data['pk_employee'])
	data = {
		'name':employee.name,
		'email':employee.email,
		'phone':employee.phone
	}
	return Response(data)



@api_view(['POST'])
def CHANGE_PHOTO_PROFILE(request):
	data = request.data
	im = Image.open(BytesIO(base64.b64decode(data['img'])))
	employee = Employee.objects.get(pk = 1)
	name_photo = str(employee.img).split('/')[1]
	im.save('./media/Img_Profile/'+str(name_photo), 'PNG')
	return Response({'Result':True})