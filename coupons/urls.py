"""urls coupons app."""

# Import django libraries
from django.urls import path

# Import controller/views
from . import views

app_name = 'coupons'
urlpatterns = [
    path('applica/', views.coupon_apply, name='apply'),
]
