from django.db import models
import os
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from influencers.models import InfluencersDetail

# Create your models here.


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"brands/{base}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class BrandDetail(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_avatar = models.ImageField(_("Brand Avatar"), upload_to=upload_to, blank=True, null=True)
    category = models.ManyToManyField('adminpanel.BrandCategory', blank=True, related_name='categories')


class BrandCategory(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    brand_category = models.CharField(max_length=100)


class HashtagDetail(models.Model):
    hashtag_name = models.CharField(max_length=100)


class CampaignDetail(models.Model):

    CAMPAIGN_TYPE = (
        ("1", "Once"),
        ("2", "Periodic")
    )

    campaign_type = models.CharField(max_length=30, choices=CAMPAIGN_TYPE)
    campaign_dates = models.ManyToManyField('adminpanel.CampaignDates', blank=True, related_name='dates')
    campaign_total_days = models.CharField(max_length=30)
    campaign_brands = models.ManyToManyField('adminpanel.BrandDetail', blank=True, related_name='brands')
    campaign_hashtags = models.ManyToManyField('adminpanel.HashtagDetail', blank=True, related_name='hashtags')
    assigned_influencers = models.ManyToManyField(InfluencersDetail, blank=True, related_name='influencers')
    is_active = models.BooleanField()


class CampaignDates(models.Model):

    WEEK_DAYS = (
        ("1", "Monday"),
        ("2", "Tuesday"),
        ("3", "Wednesday"),
        ("4", "Thursday"),
        ("5", "Friday"),
        ("6", "Saturday"),
        ("7", "Sunday")
    )

    start_datetime = models.DateTimeField()
    start_day = models.CharField(max_length=30, choices=WEEK_DAYS)
    end_datetime = models.DateTimeField()
    end_day = models.CharField(max_length=30, choices=WEEK_DAYS)
    day_count = models.CharField(max_length=30)