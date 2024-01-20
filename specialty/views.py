from django.shortcuts import render
from django.http import HttpResponse

from .models import Specialty

# Create your views here.
def index(request):
	specialties = Specialty.objects.all();
	context = {
		"specialties": specialties,
	}
	return render(request, "specialty/index.html", context);

def hospitals(request, specialty_id):
	specialty = Specialty.objects.get(pk=specialty_id)
	hospitals = specialty.hospital_set.all()
	context = {
		"hospitals": hospitals,
	}
	return render(request, "specialty/hospitals.html", context);