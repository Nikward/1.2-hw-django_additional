import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations_list = [row for row in reader]
    paginator = Paginator(stations_list, 10)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)
    context = {
            'bus_stations': page_object,
            'page': page_object,
    }
    return render(request, 'stations/index.html', context)
