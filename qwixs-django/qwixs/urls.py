from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('business/', views.BusinessList.as_view(), name='business_list'),
    path('services/', views.ServicesList.as_view(), name='services_list'),
    path('business/<int:pk>', views.BusinessDetail.as_view(), name='business_detail'),
    path('services/<int:pk>', views.ServicesDetail.as_view(), name='services_detail'),
]
