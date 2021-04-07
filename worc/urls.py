from django.contrib import admin
from django.urls import path
from rest_framework import routers
from selecao import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

router.register(r'candidate', views.CandidateViewSet, basename='candidate')

urlpatterns = [
    path('docs/', include_docs_urls(title='Api Sebrae',
                                    authentication_classes=[], permission_classes=[])),   
]

urlpatterns += router.urls