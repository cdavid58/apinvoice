from .models import Client
from company.models import Company
from data.models import *

class Create_Client:

	def CREATE_CLIENT(self,data):
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
			company = Company.objects.get(pk = data['company'])
		).save()
		return True

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
				'name': c.name,
				"phone": c.phone if c.phone is not None else 'No tiene',
				"address":c.address if c.address is not None else 'No tiene',
				'type':c.type_client
			}

	def DELETE_CLIENT(self,data):
		Client.objects.get(pk = data['pk']).delete()
		return True
			







