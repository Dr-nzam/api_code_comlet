from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Cours_api

router = DefaultRouter()
router.register('', Cours_api, basename='cours_api')

urlpatterns = [
    path('',include(router.urls))
]

