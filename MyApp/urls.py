from rest_framework import routers
from . import views
from django.urls import path, include

# create router
router = routers.DefaultRouter()
router.register(r'student', views.StudentModel, basename='api')

urlpatterns = [
    path('', include(router.urls))
]