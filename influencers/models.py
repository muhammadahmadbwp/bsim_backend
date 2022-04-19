from django.db import models
from core.models import User
import os
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{base}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class InfluencersDetail(models.Model):

    GENDER = (
        ("1", "Male"),
        ("2", "Female"),
        ("3", "Other")
    )

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='influencer_user')
    influencer_name = models.CharField(max_length=100, null=True, blank=True)
    insta_username = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    about_influencer = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey('influencers.InfluencersCategories', blank=True, on_delete=models.CASCADE, related_name='influencers_category')
    no_of_posts = models.IntegerField(blank=True, null=True)
    no_of_likes = models.IntegerField(blank=True, null=True)
    no_of_comments = models.IntegerField(blank=True, null=True)
    no_of_impressions = models.IntegerField(blank=True, null=True)
    no_of_reach = models.IntegerField(blank=True, null=True)
    children = models.ManyToManyField('influencers.InfluencersChildren', blank=True, related_name='influencers_children')
    no_of_children = models.IntegerField(blank=True, null=True)
    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True, null=True)
    interests = models.ManyToManyField('influencers.InfluencersInterests', blank=True, related_name='influencers_interest')
    service_cost = models.ManyToManyField('influencers.InfluencersServicesCost', blank=True, related_name='services_cost')
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class InfluencersChildren(models.Model):

    GENDER = (
        ("1", "Male"),
        ("2", "Female"),
        ("3", "Other")
    )

    influencer = models.ForeignKey(InfluencersDetail, blank=True, null=True, on_delete=models.CASCADE, related_name='influencers_child')
    name = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    date_of_birth = models.DateField()


class InfluencersCategories(models.Model):

    id = models.PositiveSmallIntegerField(primary_key=True, unique=True, editable=False)
    influencer_category = models.CharField(max_length=100)


class InfluencersInterests(models.Model):

    influencer_interest = models.CharField(max_length=100)


class InfluencersServicesCost(models.Model):

    service_name = models.CharField(max_length=100)
    cost_in_pkr = models.FloatField()