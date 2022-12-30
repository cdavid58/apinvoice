from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from create_invoice import Create_Invoice
import json, sqlite3, time
from client.models import Client
from .models import Invoice_FE
from send_dian import SEND_DIAN
from pos.models import Invoice_POS
from company.models import Company
from settings.models import *

@api_view(['POST'])
def CREATE_INVOICE(request):
	data = request.data
	c = Create_Invoice(data)
	result = c.value
	del c
	return Response(result)


@api_view(['POST'])
def GET_LIST_INVOICE(request):
	data = request.data
	conn = sqlite3.connect('db.sqlite3')
	cur = conn.cursor()
	query = "invoice_invoice_fe"
	if data['type'] == 2:
		query = "pos_invoice_pos"
	data = cur.execute("select DISTINCT consecutive from "+query+" where company_id = "+str(data['company'])+" order by consecutive desc limit 600").fetchall()
	_data = []
	start = time.time()
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
	print(time.time() - start)
	return Response(_data)

@api_view(['POST'])
def GET_INVOICE(request):
	data = request.data
	query = Invoice_FE
	if data['type_invoice'] == 2:
		query = Invoice_POS
	try:
		company = Company.objects.get(pk = data['company'])
	except Company.DoesNotExist:
		company = None
	_data = {}
	if company is not None:
		invoice = Invoice_FE.objects.filter(consecutive = data['consecutive'],company = company)
		_data['product'] = [
			{
				'description':i.description,
				'quanty':i.quanty,
				'price_base':i.Base_Product(),
				'tax':i.tax,
				'val_tax':i.Tax_Product(),
				'discount':i.discount,
				'subtotal':i.SubTotal_Product(),
				'total':i.Total_Product(),
				'discount_product':i.Discount_Product()
			}
			for i in invoice
		]

		invoice = invoice.last()
		_data['information'] = {
			'date':invoice.date,
			'date_expired':invoice.date_expired,
			'consecutive':invoice.consecutive,
			'payment_form':invoice.payment_form.name,

		}

		client = invoice.client
		_data['client'] = {
			'name':client.name,
			'phone':client.phone,
			'email':client.email,
			'address':client.address
		}

	return Response(_data)

@api_view(['POST'])
def Send_DIAN(request):
	data = request.data
	inv = Invoice_FE.objects.filter(consecutive = data['consecutive'])
	sd = SEND_DIAN(inv)
	return Response({'Result':sd.Operations()})


@api_view(['POST'])
def Delete_Invoice(request):
	data = request.data
	query = Invoice_FE
	company = Company.objects.get(pk = data['company'])
	if data['type_invoice'] == 2:
		query = Invoice_POS
	query.objects.filter(company = company, consecutive = data['consecutive']).delete()

@api_view(['POST'])
def GET_CONSECUTIVE(request):
	data = request.data
	if data['type_invoice'] == 1:
		query = Consecutive_FE.objects.get(company = data['company']).number
	else:
		query = Consecutive_POS.objects.get(company = data['company']).number

	return Response({'consecutive':query})