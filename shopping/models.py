from django.db import models
from inventory.models import *
from employee.models import Employee
from company.models import Company

class Shopping(models.Model):
	invoice_number = models.IntegerField()
	date = models.CharField(max_length = 12)
	employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
	total = models.FloatField(default= 0)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return str(self.invoice_number)+' '+self.employee.company.name


class List_Shopping(models.Model):
	code = models.CharField(max_length = 100)
	name = models.CharField(max_length = 150)
	quanty = models.IntegerField()
	tax = models.IntegerField(default=0)
	cost = models.FloatField()
	price_1 = models.FloatField()
	price_2 = models.FloatField(null = True, blank = True)
	price_3 = models.FloatField(null = True, blank = True)
	price_4 = models.FloatField(null = True, blank = True)
	price_5 = models.FloatField(null = True, blank = True)
	shopping = models.ForeignKey(Shopping,on_delete = models.CASCADE)