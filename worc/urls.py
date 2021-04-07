from django.contrib import admin
from django.urls import path
from rest_framework import routers
from selecao import views
router = routers.DefaultRouter()

router.register(r'candidate', views.CandidateViewSet, basename='candidate')

urlpatterns = [
    
]

urlpatterns += router.urls