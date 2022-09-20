from django.contrib import admin
from django.urls import path, include
from food import views

urlpatterns = [
    path('api/option/', views.option),
    path('api/ticket/<int:ticket_number>/', views.ticket),
    path('api/order/', views.order),
    path('admin/', admin.site.urls),
]
