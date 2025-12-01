from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloEthiopiaView.as_view()),
    path('reservation', views.home),
]