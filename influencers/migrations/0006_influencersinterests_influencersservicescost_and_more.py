# Generated by Django 4.0.2 on 2022-04-18 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0005_influencerscategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluencersInterests',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('influencer_interest', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InfluencersServicesCost',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('service_name', models.CharField(max_length=100)),
                ('cost_in_pkr', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='influencersdetail',
            name='about_influencer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='influencersdetail',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='influencers_category', to='influencers.influencerscategories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencersdetail',
            name='influencer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='influencersdetail',
            name='insta_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='influencerscategories',
            name='id',
            field=models.PositiveSmallIntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='influencerscategories',
            name='influencer_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='influencersdetail',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='influencers_interest', to='influencers.InfluencersInterests'),
        ),
        migrations.AddField(
            model_name='influencersdetail',
            name='service_cost',
            field=models.ManyToManyField(blank=True, related_name='services_cost', to='influencers.InfluencersServicesCost'),
        ),
    ]
