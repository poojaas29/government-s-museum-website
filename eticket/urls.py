from django.urls import include, path
from django.contrib import admin
from django.urls import path
from eticket.views import *

from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('services/', Services, name='services'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('booking/', Booking, name='booking'),
    path('success/', success, name='success'),
    path('book/', Book, name='book'),
    path('ngma/', ngma, name='ngma'),
    path('ticket/', Ticket, name="ticket"),

]
