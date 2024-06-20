"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views import home_view, about_view, pw_protected_view
from auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("about/", about_view),
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path("accounts/", include("allauth.urls")),
    path("protected/", pw_protected_view),
    path("protected/user-only/", auth_views.user_only_view, name="user-only"),
    path("protected/staff-only/", auth_views.staff_only_view, name="staff-only"),
]
