from django.urls import path
from .views import create_order

app_name = "order"
urlpatterns = [
    path('crear/', create_order, name='create_order'),
]
