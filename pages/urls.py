# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path('chat/', views.get_bot_response, name='chat'),
]