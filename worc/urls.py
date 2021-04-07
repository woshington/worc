from django.contrib import admin
from django.urls import path
from rest_framework import routers
from selecao import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

router.register(r'candidate', views.CandidateViewSet, basename='candidate')
router.register(r'contact', views.ContactViewSet, basename='contact')


urlpatterns = [
    path('docs/', include_docs_urls(title='Api Worc',
                                    authentication_classes=[], permission_classes=[])),   
]

urlpatterns += router.urls