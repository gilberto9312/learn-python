"""certificaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from certificaciones_python import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('periodo', views.periodo, name='periodo'),
    path('periodo/create', views.periodo_create, name='periodo_create'),
    path('periodo/<int:periodo_id>/', views.periodo_view, name='periodo_view'),
    path('periodo/<int:periodo_id>/edit', views.periodo_edit, name='periodo_edit'),
    path('periodo/<int:periodo_id>/delete', views.periodo_delete, name='periodo_delete'),
]
