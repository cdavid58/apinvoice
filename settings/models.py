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
