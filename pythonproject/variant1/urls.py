from django.urls import path
from . import views
from .views import ServiceAPIViewAccounts, ServiceAPIViewFiles, ServiceAPIViewFileAccount, page

urlpatterns = [
    path('', views.index),
    path('base', views.base),
    path('api/accounts', ServiceAPIViewAccounts.as_view()),
    path('api/files', ServiceAPIViewFiles.as_view()),
    path('api/accounts/<int:account_id>/', ServiceAPIViewFileAccount.as_view()),
    path('api/page', page)
]