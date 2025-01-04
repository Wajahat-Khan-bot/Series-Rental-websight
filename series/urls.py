from django.urls import path
from .views import index, details

app_name = 'series'
urlpatterns = [
    path('', index, name='index'),
    path('<int:series_id>', details, name='details')
]
