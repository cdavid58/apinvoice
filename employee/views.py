from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import Employee
from company.models import Company, License, Resolution_FE
import base64,sqlite3,json
from PIL import Image
from io import BytesIO
from invoice.models import Invoice_FE


@api_view(['POST'])
def Register_Employee(request):
	data = request.data
	result = False
	message = None
	company = Company.objects.get(pk = data['company'])
	try:
		employee = Employee.objects.get(documentI = data['documentI'],company = company)
		message = "already registered employee"
	except Employee.DoesNotExist as e:
		employee = None

	if employee is None:
		
		license = License.objects.get(company = company)
		if license.employee >= 1:
			try:
				Employee(
					documentI = data['documentI'],
					name = data['name'],
					phone = data['phone'],
					email = data['email'],
					user = data['user'],
					psswd = data['psswd'],
					company = company
				).save()
				result = True
				message = "Success"
				license.employee -= 1
				license.save()
			except Exception as e:
				message = e

		else:
			message = "sold out"
	print(message)
	return Response({'Result':result,'message':str(message)})

def FE(type_invoice,company):
	conn = sqlite3.connect('db.sqlite3')
	cur = conn.cursor()
	data = cur.execute("select DISTINCT consecutive from invoice_invoice_fe where company_id = "+str(company)+" order by consecutive desc limit 600").fetchall()
	_data = []
	for i in data:
		invoice = Invoice_FE.objects.filter(consecutive = i[0])
		total = 0
		for j in invoice:
			total += j.Total_Product()
		_data.append(
			{
				'pk':invoice.last().pk,
				'consecutive':i[0],
				'client':invoice.last().client.name,
				'total': total,
				"state":invoice.last().state,
				'date':invoice.last().date
			}
		)
		total = 0
	cur.close()
	return _data


@api_view(['POST'])
def Validate_Login(request):
	data = request.data
	try:
		employee = Employee.objects.get(user = data['user'], psswd=data['psswd'])
		resolution = Resolution_FE.objects.get(company = employee.company)
		result = {'result':True,'company':employee.company.pk,'employee':employee.pk,'type_employee':employee.type_employee,'prefix':resolution.prefix,'nit_company':employee.company.nit}

	except Employee.DoesNotExist:
		result = {'result':False}
	return Response(result)


@api_view(['POST'])
def GET_LIST_EMPLOYEE(request):
	data = request.data['company']
	_data = [
		{
			'pk':i.pk,
			'documentI':i.documentI,
			'name':i.name,
			'phone':i.phone,
			'email':i.email,
			'type_employee':i.type_employee
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
		'phone':employee.phone,
		'user':employee.user,
		'psswd':employee.psswd,
		'documentI':employee.documentI,
		'type_employee':employee.type_employee
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

@api_view(['POST'])
def EDIT_EMPLOYEE(request):
	data = request.data
	employee = Employee.objects.get(pk = data['pk'])
	employee.documentI = data['documentI']
	employee.name = data['name']
	employee.phone = data['phone']
	employee.email = data['email']
	employee.user = data['user']
	employee.psswd = data['psswd']
	employee.type_employee = data['type_employee']
	employee.save()
	return Response({'result':True})

@api_view(['POST'])
def DELETE_EMPLOYEE(request):
	data = request.data
	try:
		employee = Employee.objects.get(pk = data['pk'])
		license = License.objects.get(company = employee.company)
		license.employee += 1
		license.save()
		employee.delete()
		message = "El empleado se elimino con exito"
	except Employee.DoesNotExist as e:
		message = "El empleado ya fue eliminado"
	return Response({'message':message})


