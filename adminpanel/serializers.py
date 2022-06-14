from rest_framework import serializers
from adminpanel.models import (
    AdminsDetail,
    BrandCategory,
    BrandDetail,
    CampaignDetail,
    CampaignDates,
    HashtagDetail
)


class AdminsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminsDetail
        fields = "__all__"


class BrandCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BrandCategory
        fields = "__all__"


class BrandDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrandDetail
        fields = "__all__"


class CampaignDatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampaignDates
        fields = "__all__"


class HashtagDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = HashtagDetail
        fields = "__all__"


class CampaignDetailSerializer(serializers.ModelSerializer):
    campaign_dates = CampaignDatesSerializer(write_only=False, many=True)

    class Meta:
        model = CampaignDetail
        fields = "__all__"

    def create(self, validated_data):
        # print(validated_data)
        campaign_dates_data = validated_data.pop('campaign_dates', None)
        campaign_brands = validated_data.pop('campaign_brands', None)
        campaign_hashtags = validated_data.pop('campaign_hashtags', None)
        assigned_influencers = validated_data.pop('assigned_influencers', None)
        item = CampaignDetail.objects.create(**validated_data)
        item.save()
        if campaign_brands is not None:
            item.campaign_brands.set(campaign_brands)
        if campaign_hashtags is not None:
            item.campaign_hashtags.set(campaign_hashtags)
        if assigned_influencers is not None:
            item.assigned_influencers.set(assigned_influencers)
        campaign_days = []
        if campaign_dates_data is not None:
            for date_x in campaign_dates_data:
                date_x_data = CampaignDates.objects.create(**date_x)
                date_x_data.save()
                campaign_days.append(date_x_data)
                item.campaign_dates.add(*campaign_days)
        return item

