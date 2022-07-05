from rest_framework import serializers
from adminpanel.models import (
    AdminsDetail,
    # BrandCategory,
    BrandDetail,
    CampaignDetail,
    CampaignDates,
    HashtagDetail
)
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import IntegerField
from datetime import datetime as dt

class AdminsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminsDetail
        fields = "__all__"


# class BrandCategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = BrandCategory
#         fields = "__all__"


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
            campaign_days_count = 0
            for date_x in campaign_dates_data:
                # days = (dt.strptime(date_x.get('end_datetime'), '%Y-%m-%d %X') - dt.strptime(date_x.get('start_datetime'), '%Y-%m-%d %X').days)
                days = (date_x.get('end_datetime') - date_x.get('start_datetime')).days
                campaign_days_count += days
                date_x['day_count'] = days
                date_x_data = CampaignDates.objects.create(**date_x)
                date_x_data.save()
                campaign_days.append(date_x_data)
                item.campaign_dates.add(*campaign_days)
        item.campaign_total_days = campaign_days_count
        item.total_campaigns = len(campaign_dates_data)
        item.total_influencers = len(assigned_influencers)
        item.campaign_start_date = min([x['start_datetime'] for x in campaign_dates_data])
        item.campaign_end_date = max([x['end_datetime'] for x in campaign_dates_data])
        item.save()
        return item


class GetCampaignDetailSerializer(serializers.ModelSerializer):
    campaign_dates = CampaignDatesSerializer(write_only=False, many=True)

    class Meta:
        model = CampaignDetail
        fields = "__all__"
        depth = 1


class FilterCampaignsSerializer(serializers.ModelSerializer):
    # total_campaigns = serializers.SerializerMethodField()
    # total_influencers = serializers.SerializerMethodField()
    # total_campaign_days = serializers.SerializerMethodField()

    class Meta:
        model = CampaignDetail
        fields = "__all__"
        depth = 1

    # def get_total_campaigns(self, instance):
    #     return instance.campaign_dates.count()

    # def get_total_influencers(self, instance):
    #     return instance.assigned_influencers.count()

    # def get_total_campaign_days(self, instance):
    #     return CampaignDetail.objects.values('campaign_dates__day_count').filter(
    #         id=instance.id
    #         ).annotate(campaign_days=Cast('campaign_dates__day_count', IntegerField())).aggregate(
    #             Sum('campaign_days')
    #             ).get('campaign_days__sum')