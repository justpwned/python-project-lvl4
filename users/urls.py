from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('create/', SignUpView, name='create_user')
]
