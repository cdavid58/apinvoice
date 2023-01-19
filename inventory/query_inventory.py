from .models import *
from django.db.models import Q

class Query_Inventory:
	def Create_Inventory(self,data):
		Inventory(
			code = data['code'],
			name = data['name'].lower(),
			quanty = data['quanty'],
			tax = data['tax'],
			cost = data['cost'],
			price_1 = data['price_1'],
			price_2 = data['price_2'],
			price_3 = data['price_3'],
			price_4 = data['price_4'],
			price_5 = data['price_5'],
			supplier = Supplier.objects.get(pk = data['supplier']),
			subcategory = SubCategory.objects.get(pk = data['subcategory']),
			company = Company.objects.get(pk = data['company'])
		).save()

	def GET_PRODUCT(self,data):
		_data = {}
		try:
			company = Company.objects.get(pk = data['company'])
			product = Inventory.objects.get( Q(code__contains = data['value']) | Q(name__icontains = data['value']), company = company )
			print(product.code)
			_data = {
					"code":product.code,
					"name":product.name,
					"quanty":product.quanty,
					"tax":product.tax,
					"cost":product.cost,
					"price_1":product.price_1,
					"price_2":product.price_2,
					"price_3":product.price_3,
					"price_4":product.price_4,
					"price_5":product.price_5
				}
		except Inventory.DoesNotExist as e:
			print(e)
		return _data

	def GET_LIST_INVENTORY(self,data):
		return [
			{
				'pk':i.pk,
				'code':i.code,
				'name':i.name,
				'quanty':i.quanty,
				'tax':i.tax,
				"cost":i.cost,
				'price_1':i.price_1,
				'price_2':i.price_2,
				'price_3':i.price_3,
				'price_4':i.price_4,
				'price_5':i.price_5
			}
			for i in Inventory.objects.filter(company = Company.objects.get(pk = data['company']))
		]

	def UPDATED_PRODUCT(self,data):
		try:
			inventory = Inventory.objects.get(company = Company.objects.get(pk = data['company']),pk = data['pk'])
		except Inventory.DoesNotExist as e:
			message = "El producto no existe"
			inventory = None

		if inventory is not None:
			inventory.name = data['name']
			inventory.tax = data['tax']
			inventory.cost = data['cost']
			inventory.price_1 = data['price_1']
			inventory.price_2 = data['price_2']
			inventory.price_3 = data['price_3']
			inventory.price_4 = data['price_4']
			inventory.price_5 = data['price_5']
			inventory.save()
			return {'result':True,'message':"Updated Product"}
		return {'result':False,'message':message}

	def DELETE_PRODUCT(self,data):
		try:
			Inventory.objects.get(company = Company.objects.get(pk = data['company']),code = data['code']).delete()
			result = True
		except Exception as e:
			result = False
		return result

