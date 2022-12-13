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
			company = Company.objects.get(nit = data['company'])
		).save()

	def GET_PRODUCT(self,data):
		_data = {}
		try:
			product = Inventory.objects.get( Q(code__contains = data['value']) | Q(name__icontains = data['value']) )
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
		except Inventory.DoesNotExist:
			pass
		return _data

	def GET_LIST_INVENTORY(self,data):
		return [
			{
				'pk':i.pk,
				'name':i.name,
				'quanty':i.quanty,
				'price_1':i.price_1,
				'price_2':i.price_2,
				'price_3':i.price_3,
				'price_4':i.price_4,
				'price_5':i.price_5
			}
			for i in Inventory.objects.filter(company = Company.objects.get(nit = data['company']))
		]
