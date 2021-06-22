from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('services/', views.services, name='services'),
    path('order/', views.order, name='order'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail')
]