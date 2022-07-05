from celery import shared_task
from adminpanel.models import CampaignDetail, CampaignDates
from django.db.models import Q
from datetime import datetime


@shared_task()
def add(x, y):
    return x + y


@shared_task()
def campaign_status_update():

    queryset = CampaignDetail.objects.filter(
        Q(campaign_status = 1) | Q(campaign_status = 2)
        ).prefetch_related('campaign_dates')
    for qs in queryset:
        days_completed = 0
        for x in qs:
            if x.get('start_datetime') <= datetime.now() <= x.get('end_datetime'):
                qs.campaign_status = 1
                days_completed += (datetime.now() - x.get('start_datetime')).days
            elif (datetime.now() < x.get('start_datetime') or datetime.now() > x.get('end_datetime')) and x.get('end_datetime') < qs.campaign_end_date:
                qs.campaign_status = 2
                days_completed += (x.get('end_datetime') - x.get('start_datetime')).days
            elif datetime.now() > qs.campaign_end_date:
                qs.campaign_status = 3
                days_completed += (qs.campaign_end_date - qs.campaign_start_date).days
        
        qs.campaign_completed_days = days_completed



        print(qs.campaign_dates.values())

    return 'hello'