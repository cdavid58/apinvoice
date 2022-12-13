from django.db import models
from company.models import Company

class Employee(models.Model):
	documentI = models.CharField(max_length = 12, unique = True)
	name = models.CharField(max_length = 40)
	phone = models.CharField(max_length = 12)
	email = models.EmailField()
	user = models.CharField(max_length = 20, unique = True)
	psswd = models.CharField(max_length = 20, unique = True)
	block = models.BooleanField(default = False)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

	def __str__(self):
		return self.name+' | '+self.company.name

	def Validate_Login(self,user,psswd):
		try:
			employee = Employee.objects.get(user = user, psswd=psswd)
			result = True
		except Employee.DoesNotExist:
			result = False
		return result
		
		






