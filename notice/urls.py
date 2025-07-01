from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notices, name='view_notices'),
    path('upload/', views.upload_notice, name='upload_notice'),
]
