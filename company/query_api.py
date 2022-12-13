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
		

	def Create_License(self):
		try:
			today = datetime.datetime.utcnow()
			License(
				price = self.data['price'],
				date_payment = today,
				dete_experied = today + datetime.timedelta(days=365),
				company = Company.objects.get(nit = self.data['nit'])
			).save()
			result = True
		except Exception as e:
			print(e)
			result = False
		return result
		





