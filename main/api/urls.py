from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'search-specific', views.specificsearchViewset, base_name="Demo")

urlpatterns = [
    path('', include(router.urls), name='index'),
]
