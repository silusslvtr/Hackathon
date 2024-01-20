from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Hospital

# Create your views here.
def index(request):
	hospitals = Hospital.objects.all()
	context = {
		"hospitals": hospitals,
	}
	return render(request, "hospital/index.html", context)

def Json_Response(request):
	hospitals = Hospital.objects.all()

	data = {}

	for obj in hospitals:
		hospital = {}
		hospital['id'] = obj.id
		hospital['name'] = obj.name

		for doctor in obj.doctors.all():
			doctors = {}
			doctors['id'] = doctor.id
			doctors['name'] = doctor.name

		hospital['doctors'] = doctors

		data[obj.id] = hospital

	return JsonResponse(data)