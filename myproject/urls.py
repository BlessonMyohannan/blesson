"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h/<str:myname>', views.home),
     path('a/<str:m>', views.about),
    path('add/',views.addStud),
    path('new',views.viewStud),
    path('del/<int:sid>', views.delStud),
    path('edit/<int:sid>', views.edit_stud),
     path('addemp/', views.addEmp),
    path('addemp/', views.addEmp),
    path('viewemp/', views.viewEmp),
]

