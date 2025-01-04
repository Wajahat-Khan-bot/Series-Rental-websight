from django.db import models
from tastypie.resources import ModelResource
from series.models import Series


class SerieResource(ModelResource):
    class Meta:
        queryset = Series.objects.all()
        resource_name = 'series'
