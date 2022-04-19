from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='userview-api')
router.register(r'userauth', views.AuthUserViewSet, basename='authuser-api')
urlpatterns = [
    path('', include(router.urls)),
]