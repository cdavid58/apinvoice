from django.db import models
from company.models import Company

class Consecutive_FE(models.Model):
	number = models.IntegerField(default = 1)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

	def __str__(self):
		return self.company.name

class Consecutive_POS(models.Model):
	number = models.IntegerField(default = 1)
	company = models.ForeignKey(Company, on_delete = models.CASCADE)

	def __str__(self):
		return self.company.name

class Value_Hour_Extra(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length = 80)


class Value_Vacation(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length = 80)

class Work_Disabilities(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length = 80)


