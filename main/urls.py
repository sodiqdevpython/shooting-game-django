from django.urls import path
from .views import starting, detail

urlpatterns = [
    path('', starting, name='starting'),
    path('game/<int:pk>/', detail, name='detail')
]