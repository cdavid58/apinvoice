from .models import Client
from company.models import Company
from data.models import *

class Create_Client:

	def CREATE_CLIENT(self,data):
		try:
			company = Company.objects.get(pk = data['company'])
			client = Client.objects.get(identification_number = data['identification_number'],company = company)
			message = "The client is already registered"
			result = False
		except Client.DoesNotExist as e:
			client = None
			print(e)
		if len(data['identification_number']) == 7 or  len(data['identification_number']) == 10:
			if client is None:
				Client(
					identification_number = data['identification_number'],
					dv = data['dv'],
					name = data['name'],
					phone = data['phone'],
					address = data['address'],
					email = data['email'],
					merchant_registration = data['merchant_registration'],
					type_documentI = Type_Document_Identification.objects.get(pk = data['type_documentI']),
					type_organization = Type_Organization.objects.get(pk = data['type_organization']),
					type_regime = Type_Regime.objects.get(pk = data['type_regime']),
					municipality = Municipality.objects.get(pk = data['municipality']),
					company = company
				).save()
				result = True
				message = "Success"
		else:
			result = False
			message = "Documento I errado"
		return {"result":result,'message':message}
		
	def GET_LIST_CLIENT(self,data):
		return [
			{
				'pk':i.pk,
				'name': i.name,
				'address':i.address if i.address is not None and i.address != "" else "No tiene",
				'email':i.email if i.email is not None and i.email != "" else "No tiene",
				'documentI':i.identification_number,
				'phone':i.phone if i.phone is not None and i.phone != "" else "No tiene"
			}
			for i in Client.objects.filter(company = Company.objects.get(pk = data['company']))
		]

	def GET_CLIENT(self,data):
		c = Client.objects.get(pk = data['pk'])
		return{
				'pk': c.pk,
				'identification_number': c.identification_number,
				'dv': c.dv,
				'name': c.name,
				"phone": c.phone if c.phone is not None and c.phone != "" else 'No tiene',
				"address":c.address if c.address is not None and c.address != "" else 'No tiene',
				'email':c.email if c.email is not None and c.email != "" else "No tiene",
				'type':c.type_client,
				"merchant_registration":c.merchant_registration if c.merchant_registration is not None and c.merchant_registration != "" else "No tiene",
				'type_documentI_name':c.type_documentI.name,
				'type_documentI_pk':c.type_documentI.pk,
				'type_organization_name':c.type_organization.name,
				'type_organization_pk':c.type_organization.pk,
				'type_regime_name':c.type_regime.name,
				'type_regime_pk':c.type_regime.pk,
				'municipality_name':c.municipality.name,
				'municipality_pk':c.municipality.pk,
				'type_client':c.type_client
			}

	def DELETE_CLIENT(self,data):
		Client.objects.get(pk = data['pk']).delete()
		return True
			
	def EDIT_CLIENT(self,data):
		result = False
		try:
			client = Client.objects.get(pk = data['pk'])
		except Client.DoesNotExist as e:
			client = None
			message = str(e)

		if client is not None:

			client.identification_number = data['identification_number']
			client.dv = data['dv']
			client.name = data['name']
			client.phone = data['phone']
			client.address = data['address']
			client.email = data['email']
			client.merchant_registration = data['merchant_registration']
			client.type_documentI = Type_Document_Identification.objects.get(pk = data['type_documentI'])
			client.type_organization = Type_Organization.objects.get(pk = data['type_organization'])
			client.type_regime = Type_Regime.objects.get(pk = data['type_regime'])
			client.municipality = Municipality.objects.get(pk = data['municipality'])
			client.type_client = data['type_client']
			client.save()
			result = True
			message = "Client Updated"
		
		return {'result':result,'message':message}







