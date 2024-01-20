from django.db import models
from specialty.models import Specialty

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=75)
	specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

	def __str__(self):
		return self.name