from django.urls import path
from .views import signup


urlpatterns = [
    path('user-create', signup, name='signup'),
]