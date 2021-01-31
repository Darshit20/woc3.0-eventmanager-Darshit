from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('event-registration', views.eventReg),
    path('participants-registration', views.participantsReg),
    path('dashboard-login', views.dashboardLogin),
    path('dashboard-logout', views.dashboardLogout),
]
