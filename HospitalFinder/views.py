from django.shortcuts import render, redirect


def HOME(request):
    return render(request, 'base.html')


def HOSPITAL(request):
    return render(request, 'hospital.html')
