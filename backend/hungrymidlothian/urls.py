from django.contrib import admin
from django.urls import path, include
from food import views

urlpatterns = [
    path('api/options/', views.option_list),
    path('admin/', admin.site.urls),
]
