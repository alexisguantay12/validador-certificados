from django.urls import path
from .views import validador

urlpatterns = [

    path("validador/", validador, name="validador_certificados"),

]