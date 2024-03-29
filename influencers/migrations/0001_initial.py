# Generated by Django 4.0 on 2022-02-16 16:36

from django.db import migrations, models
import django.db.models.deletion
import influencers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_user_otp_user_otp_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluencerCategories',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InfluencersChildren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=30)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InfluencersDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=30)),
                ('no_of_posts', models.IntegerField(blank=True, null=True)),
                ('no_of_likes', models.IntegerField(blank=True, null=True)),
                ('no_of_comments', models.IntegerField(blank=True, null=True)),
                ('no_of_impressions', models.IntegerField(blank=True, null=True)),
                ('no_of_reach', models.IntegerField(blank=True, null=True)),
                ('no_of_children', models.IntegerField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=influencers.models.upload_to, verbose_name='Avatar')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('children', models.ManyToManyField(blank=True, related_name='influencers_children', to='influencers.InfluencersChildren')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='influencer_user', to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='influencerschildren',
            name='influencer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='influencers_child', to='influencers.influencersdetail'),
        ),
    ]
