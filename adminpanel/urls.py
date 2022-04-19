from django.urls import path, include
from adminpanel import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'brand_category', views.BrandCategoryViewSet, basename='brand-category-api')
router.register(r'brand_detail', views.BrandDetailViewSet, basename='brand-detail-api')
router.register(r'campaign_detail', views.CampaignDetailViewSet, basename='campaign-detail-api')
router.register(r'hashtag_detail', views.HashtagDetailViewSet, basename='hashtag-detail-api')

urlpatterns = [
    path('', include(router.urls)),
]