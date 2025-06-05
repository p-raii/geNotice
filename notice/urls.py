from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_notice, name='upload_notice'),
    path('view/', views.view_notices, name='view_notices'),
]
