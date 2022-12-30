from django.db import models
from data.models import *
from company.models import *

class Client(models.Model):
	identification_number = models.IntegerField()
	dv = models.IntegerField(blank=True,null=True)
	name = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 15, null= True, blank=True)
	address = models.TextField(blank=True,null=True)
	email = models.TextField(blank=True,null=True)
	merchant_registration = models.CharField(max_length = 15, blank=True,null=True)
	type_documentI = models.ForeignKey(Type_Document_Identification,on_delete = models.CASCADE, blank=True,null=True)
	type_organization = models.ForeignKey(Type_Organization,on_delete=models.CASCADE, blank=True,null=True)
	type_regime = models.ForeignKey(Type_Regime,on_delete=models.CASCADE, blank=True,null=True)
	municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE, blank=True,null=True)
	company = models.ForeignKey(Company,on_delete=models.CASCADE)
	type_client = models.IntegerField(default = 1)

	def __str__(self):
		return self.name+' | '+self.company.name

