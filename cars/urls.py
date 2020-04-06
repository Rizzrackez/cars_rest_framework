from django.urls import path
from cars.views import *

app_name = 'car'

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/list/', CarListView.as_view()),
    path('car/<int:pk>/',  CarDetailView.as_view()),
]


