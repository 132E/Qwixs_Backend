from django.urls import path, re_path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('owner/', views.OwnerList.as_view(), name='owner_list'),
    path('business/', views.BusinessList.as_view(), name='business_list'),
    path('services/', views.ServicesList.as_view(), name='services_list'),
    path('owner/<int:pk>/', views.OwnerDetail.as_view(), name='owner_detail'),
    path('business/<int:pk>', views.BusinessDetail.as_view(), name='business_detail'),
    path('services/<int:pk>', views.ServicesDetail.as_view(), name='services_detail'),
]
