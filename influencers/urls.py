from django.urls import path, include
from influencers import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'influencers_detail', views.InfluencersDetailViewSet, basename='influencers-detail-api')

urlpatterns = [
    path('', include(router.urls)),
]