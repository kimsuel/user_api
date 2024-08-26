from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, AddressViewSet

router = DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)
router.register('address', AddressViewSet)

urlpatterns = [
] + router.urls
