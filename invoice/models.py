from django.db import models
from company.models import Company
from employee.models import Employee
from client.models import Client
from settings.models import *
from data.models import *


class Invoice_FE(models.Model):
	consecutive = models.IntegerField()
	code = models.IntegerField()
	description = models.CharField(max_length = 100)
	price = models.FloatField()
	tax = models.FloatField()
	discount = models.FloatField()
	quanty = models.FloatField()
	date = models.CharField(max_length = 10)
	date_expired = models.CharField(max_length = 10)
	time = models.CharField(max_length = 10)
	payment_form = models.ForeignKey(Payment_Form, on_delete = models.CASCADE)
	cancelled = models.BooleanField(default = True)
	employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)
	state = models.TextField(default = "Sin enviar a la DIAN")

	def __str__(self):
		return self.company.name+' | '+str(self.consecutive)

	def Base_Product(self):
		base = self.price / ( 1 + ( self.tax / 100 ))
		base_with_discount = base * (self.discount / 100)
		return round(base - base_with_discount,1)

	def Discount_Product(self):
		base = self.price / ( 1 + ( self.tax / 100 ))
		return round(base * (self.discount / 100),1)


	def Tax_Product(self):
		return round( (self.Base_Product() * (self.tax / 100)) * self.quanty,1)

	def SubTotal_Product(self):
		return round(self.Base_Product() * self.quanty,1)

	def Total_Product(self):
		return round( ( self.Base_Product() + (self.Tax_Product() / self.quanty)  ) * self.quanty,1)


class Wallet_FE(models.Model):
	invoice = models.ForeignKey(Invoice_FE, on_delete = models.CASCADE)
	cancelled = models.BooleanField(default = False)
	days_in_debt = models.IntegerField(default = 0)
	employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

