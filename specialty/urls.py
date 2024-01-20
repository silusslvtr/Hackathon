from django.urls import path
from . import views

app_name = 'specialty'

urlpatterns = [
	path("", views.index, name="specialty"),
	path("<int:specialty_id>/view_hospitals", views.hospitals, name="hospitals"),
]