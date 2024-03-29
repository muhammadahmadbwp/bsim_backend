# Generated by Django 4.0.2 on 2022-02-25 15:51

import adminpanel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('influencers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCategory',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BrandDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_avatar', models.ImageField(blank=True, null=True, upload_to=adminpanel.models.upload_to, verbose_name='Brand Avatar')),
                ('category', models.ManyToManyField(blank=True, related_name='categories', to='adminpanel.BrandCategory')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('start_day', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=30)),
                ('end_datetime', models.DateTimeField()),
                ('end_day', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=30)),
                ('day_count', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HashtagDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_type', models.CharField(choices=[('1', 'Once'), ('2', 'Periodic')], max_length=30)),
                ('campaign_total_days', models.CharField(max_length=30)),
                ('is_active', models.BooleanField()),
                ('assigned_influencers', models.ManyToManyField(blank=True, related_name='influencers', to='influencers.InfluencersDetail')),
                ('campaign_brands', models.ManyToManyField(blank=True, related_name='brands', to='adminpanel.BrandDetail')),
                ('campaign_dates', models.ManyToManyField(blank=True, related_name='dates', to='adminpanel.CampaignDates')),
                ('campaign_hashtags', models.ManyToManyField(blank=True, related_name='hashtags', to='adminpanel.HashtagDetail')),
            ],
        ),
    ]
