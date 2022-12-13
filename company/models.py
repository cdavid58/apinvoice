from django.db import models

class Company(models.Model):
	nit = models.CharField(max_length=12, unique= True)
	name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 150)
	email = models.EmailField(unique= True)
	phone = models.CharField(max_length = 20)
	phone_2 = models.CharField(max_length = 20)
	block = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class License(models.Model):
	price = models.FloatField(default = 0)
	date_payment = models.CharField(max_length = 12)
	dete_experied = models.CharField(max_length = 12)
	company = models.ForeignKey(Company, on_delete= models.CASCADE)

	def __str__(self):
		return self.company.name


class Resolution_POS(models.Model):
	prefix = models.CharField(max_length = 5)
	resolution = models.IntegerField(max_length = 12)
	from_number = models.IntegerField(max_length = 10)
	from_number = models.IntegerField(max_length = 10)
	date_from = models.CharField(max_length = 10)
	date_to = models.CharField(max_length = 10)
	token = models.CharField(max_length = 100)
	company = models.ForeignKey(Company, on_delete= models.CASCADE)

	def __str__(self):
		return self.company.name


class Resolution_FE(models.Model):
	prefix = models.CharField(max_length = 5)
	resolution = models.IntegerField(max_length = 12)
	from_number = models.IntegerField(max_length = 10)
	from_number = models.IntegerField(max_length = 10)
	date_from = models.CharField(max_length = 10)
	date_to = models.CharField(max_length = 10)
	company = models.ForeignKey(Company, on_delete= models.CASCADE)

	def __str__(self):
		return self.company.name

