from django.urls import path
from .views import validador

urlpatterns = [

    path("autogestion/validador_certificados/", validador, name="validador_certificados"),

]