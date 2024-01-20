from django.db import models
from doctor.models import Doctor
from specialty.models import Specialty

# Create your models here.
class Hospital(models.Model):
	name = models.CharField(max_length=75)
	doctor = models.ManyToManyField(Doctor)
	specialty = models.ManyToManyField(Specialty)

	def __str__(self):
		return self.name