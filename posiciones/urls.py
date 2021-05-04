from django.urls import path
from . import views

urlpatterns = [
    path('bolsaDeTrabajoHome', views.home, name="bolsaDeTrabajoHome"),
]
