from .models import *
from employee.models import Employee
from company.models import Company
from inventory.models import Inventory
import json

class CREATE_SHOPPING:
	def __init__(self,data):
		self.data = data

	def Create_Shopping(self):
		try:
			shopping = Shopping.objects.get(invoice_number = self.data['shopping']['invoice_number'],company = Employee.objects.get(pk = self.data['shopping']['employee']).company)
			result = False
		except Shopping.DoesNotExist as e:
			print(e)
			shopping = None

		if shopping is None:
			self.employee = Employee.objects.get(pk = self.data['shopping']['employee'])
			Shopping(
				invoice_number = self.data['shopping']['invoice_number'],
				date = self.data['shopping']['date'],
				employee = self.employee,
				total = self.data['shopping']['total'],
				company = self.employee.company
			).save()
			self.Create_Shopping_List()
			result = True
		return {'result':result}

	def Create_Shopping_List(self):
		for i in self.data['shopping_lines']:
			data = json.loads(i)
			print(data)
			for j in data:
				List_Shopping(
					code = j['CODIGO'],
					name = j['DESCRIPCION'],
					quanty = j['CANTIDAD'],
					tax = j['IVA'],
					cost = j['COSTO'],
					price_1 = j['P1'],
					price_2 = j['P2'],
					price_3 = j['P3'],
					price_4 = j['P4'],
					price_5 = j['P5'],
					shopping = Shopping.objects.get(invoice_number = self.data['shopping']['invoice_number'],company = self.employee.company)
				).save()
				print(self.employee.company)
				inventory = Inventory.objects.get(code = "003")
				inventory.quanty += int(j['CANTIDAD'])
				inventory.tax = int(j['IVA'])
				inventory.cost = float(j['COSTO'])
				inventory.price_1 = float(j['P1'])
				inventory.price_2 = float(j['P2'])
				inventory.price_3 = float(j['P3'])
				inventory.price_4 = float(j['P4'])
				inventory.price_5 = float(j['P5'])
				inventory.save()

	def CHECK_INVOICE_NUMBER(self):
		try:
			company = Company.objects.get(pk = self.data['company'])
			shopping = Shopping.objects.get(invoice_number = self.data['invoice_number'],company = company)
			result = True
		except Shopping.DoesNotExist as e:
			result = False
		return result
		




