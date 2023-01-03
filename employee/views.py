from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import Employee
from company.models import Company
import base64,sqlite3,json
from PIL import Image
from io import BytesIO
from invoice.models import Invoice_FE

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
		result = {'result':True,'company':employee.company.pk,'employee':employee.pk}
		# try:
		# 	invoice_fe = Invoice_FE.objects.filter(company = employee.company)
		# except Invoice_FE.DoesNotExist:
		# 	invoice_fe = None
		# if invoice_fe is not None:
		# 	data = FE(1,employee.company.pk)
		# 	with open('./static/data_fe.json', 'w') as file:
		# 		json.dump(data, file, indent=4)

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