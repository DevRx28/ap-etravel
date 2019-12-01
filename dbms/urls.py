"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views as auth_views

from gobabygo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='Home'),
    path('flights/', views.flights_page, name='Flights'),
    path('login/', views.login_page, name='Login'),
    path('login/', include('social_django.urls', namespace='social')),
    path('signup/', views.signup_page, name='Signup'),
    path('hotels/', views.hotels_page, name='Hotels'),
    path('book/', views.booking_page, name='Booking'),
    path('account/', views.account, name='Account'),
    path('logout/', views.logout, name='LogOut')
]
