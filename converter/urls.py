from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('download/<str:file_name>/', views.download_dtl, name='download_dtl'),
]