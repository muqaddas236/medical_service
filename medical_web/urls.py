from django.contrib import admin
from django.urls import path
from medical_service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('robot/', views.robot_page),
    path('mskt/', views.mskt_page),
    path('ask-ai/', views.ask_ai),
]