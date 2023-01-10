from .models import *
import datetime

class Query_Company:

	def __init__(self, data):
		self.data = data

	def Create_Company(self):
		try:
			Company(
				nit = self.data['nit'],
				name = self.data['name'],
				address = self.data['address'],
				email = self.data['email'],
				phone = self.data['phone'],
				phone_2 = self.data['phone_2']
			).save()
			result = True
		except Exception as e:
			result = False
		return result
		
	def Licenses(self):
		document_annual = 0
		employee = 0
		#LOS PRECIOS SON MENSUALES
		if int(self.data['price']) == 0:
			document_annual = 9
			employee = 1
		elif int(self.data['price']) == 15000:
			document_annual = 25
			employee = 1
		elif int(self.data['price']) == 22000:
			document_annual = 50
			employee = 1
		elif int(self.data['price']) == 46500:
			document_annual = 500
			employee = 1
		elif int(self.data['price']) == 150000:
			document_annual = 6000
			employee = 5
		elif int(self.data['price']) == 166670:
			document_annual = 8000
			employee = 5
		elif int(self.data['price']) == 250000:
			document_annual = 100000
			employee = 50
		return [document_annual,employee]

	def Create_License(self):
		try:
			today = datetime.datetime.utcnow()
			lic = self.Licenses()
			License(
				price = self.data['price'],
				date_payment = today,
				dete_experied = today + datetime.timedelta(days=365),
				document_annual = lic[0],
				employee = lic[1],
				company = Company.objects.get(nit = self.data['nit'])
			).save()
			result = True
		except Exception as e:
			print(e)
			result = False
		return result
		





