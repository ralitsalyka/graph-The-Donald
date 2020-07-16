from django.shortcuts import render
from dataHolder.data import *
from dataHolder.help_functions import *
import pymongo


def index(request):
    return render(request, 'index.html', {'data': data})


def week_stat(request):
    return render(request, 'week_stat.html', {'data_week': data_week})


def week_stat2014(request):
    return render(request, 'week_stat2014.html', {'data_week2014': data_week2014})


def week_stat2015(request):
    return render(request, 'week_stat2015.html', {'data_week2015': data_week2015})


def week_stat2016(request):
    return render(request, 'week_stat2016.html', {'data_week2016': data_week2016})


def week_stat2017(request):
    return render(request, 'week_stat2017.html', {'data_week2017': data_week2017})


def week_stat2018(request):
    return render(request, 'week_stat2018.html', {'data_week2018': data_week2018})


def week_stat2019(request):
    return render(request, 'week_stat2019.html', {'data_week2019': data_week2019})


def week_stat2020(request):
    return render(request, 'week_stat2020.html', {'data_week2020': data_week2020})


def mood(request):
    return render(request, 'mood.html', {'happy': data_for_happy, 'angry': data_for_angry})
