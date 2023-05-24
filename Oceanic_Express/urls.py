"""Oceanic_Express URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from oceanicexpress import views


urlpatterns = [
    path('', views.home, name= "home"),
    path('signup/', views.signups, name= "signup"),
    path('login/', views.logins, name= "login"),
    path('logout/', views.admin_logout, name='logout'),
    path('admin/login/', views.admin_login, name= "admin_login"),
    path('admin/dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin/add_package/', views.admin_add_package, name="add_package"),
    path('admin/update_package/<int:id>/', views.admin_update_package, name="update_package"),
    path('delete/<int:id>/', views.delete_package, name="delete_package"),
    path('superadmin/', admin.site.urls)
]
