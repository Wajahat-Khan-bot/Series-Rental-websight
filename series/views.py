from django.shortcuts import render, get_object_or_404
from .models import Series
from django.http import HttpResponse, Http404


def index(request):
    series = Series.objects.all()
    return render(request, 'series/index.html', {'series': series})


def details(request, series_id):
        serie = get_object_or_404(Series, pk=series_id)
        return render(request, 'series/details.html', {'serie': serie})
