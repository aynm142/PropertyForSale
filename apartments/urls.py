from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('user-create', SignUpView.as_view()),
]