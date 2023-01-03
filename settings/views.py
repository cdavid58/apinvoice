from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from data.models import *


@api_view(['POST'])
def Type_DocumentI(request):
	data = [
		{
			'pk':i._id,
			'name':i.name
		}
		for i in Type_Document_Identification.objects.all()
	]
	return Response(data)



@api_view(['POST'])
def Type_Organizations(request):
	data = [
		{
			'pk':i._id,
			'name':i.name
		}
		for i in Type_Organization.objects.all()
	]
	return Response(data)



@api_view(['POST'])
def Type_Regimen(request):
	data = [
		{
			'pk':i._id,
			'name':i.name
		}
		for i in Type_Regime.objects.all()
	]
	return Response(data)


@api_view(['POST'])
def Municipalitys(request):
	data = [
		{
			'pk':i._id,
			'name':i.name
		}
		for i in Municipality.objects.all()
	]
	return Response(data)

@api_view(['POST'])
def Type_Documents(request):
	data = [
		{
			'pk':i._id,
			'name':i.name
		}
		for i in Type_Document.objects.all()
	]
	return Response(data)