from django.urls import include, path
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'manufacturer', views.ManufacturerViewSet)
router.register(r'shoetype', views.ShoeTypeViewSet)
router.register(r'shoecolor', views.ShoeColorViewSet)
router.register(r'shoe', views.ShoeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
