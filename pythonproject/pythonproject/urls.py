"""
URL configuration for pythonproject project.

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
from rest_framework import routers
from variant1 import views as main_views
from variant1.views import AccountsCreateView, AccountsUpdateView, AccountsListView
from variant1.views import FilesCreateView, FilesUpdateView, FilesListView
from django.views.generic import TemplateView
router = routers.DefaultRouter()
router.register(r'users', main_views.UserViewSet)
router.register(r'groups', main_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('variant1/', include('variant1.urls')),
    path('listfile/', FilesListView.as_view(), name='files_list'),
    path('addfile/', FilesCreateView.as_view(), name='file_add'),
    path('<int:pk>/editfile/', FilesUpdateView.as_view(), name='file_edit'),
    path('list/', AccountsListView.as_view(), name='account_list'),
    path('add/', AccountsCreateView.as_view(), name='account_add'),
    path('<int:pk>/edit/', AccountsUpdateView.as_view(), name='account_edit'),
    path('files/<int:file_id>/', main_views.get_file_by_id, name='get_file_by_id'),
    path('user-files/<int:account_id>/', main_views.get_account_files, name='get_account_files'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('secure/', main_views.secure_page, name='secure_page')
]
