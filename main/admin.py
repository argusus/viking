from django.contrib import admin
from .models import ServicesAndPrice, Questions, OrderServices


@admin.register(ServicesAndPrice)
class ServiceAndPriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'si', 'description')


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('tel', 'name', 'text_questions', 'time_question')
    list_filter = ('tel', 'name', 'time_question')
    search_fields = ('tel', 'name', 'time_question')
    prepopulated_fields = {'tel': ('name',)}


@admin.register(OrderServices)
class OrderServicesAdmin(admin.ModelAdmin):
    list_display = ('tel_service', 'name_service', 'text_service', 'time_service')
    list_filter = ('tel_service', 'name_service', 'time_service')
    search_fields = ('tel_service', 'name_service', 'time_service')
    prepopulated_fields = {'tel_service': ('name_service',)}
