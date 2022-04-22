from rest_framework import serializers
from influencers.models import (
    InfluencersDetail,
    InfluencersChildren,
    InfluencersCategories,
    InfluencersInterests,
    InfluencersServicesCost
)


class InfluencersChildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencersChildren
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.pop('name', instance.name)
        instance.gender = validated_data.pop('gender', instance.gender)
        instance.date_of_birth = validated_data.pop('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance


class InfluencersCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencersCategories
        fields = "__all__"


class InfluencersInterestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencersInterests
        fields = "__all__"


class InfluencersServicesCostSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencersServicesCost
        fields = "__all__"


class InfluencersDetailSerializer(serializers.ModelSerializer):
    children = InfluencersChildrenSerializer(write_only=True, many=True)
    interests = InfluencersInterestsSerializer(write_only=True, many=True)
    service_cost = InfluencersServicesCostSerializer(write_only=True, many=True)

    class Meta:
        model = InfluencersDetail
        fields = "__all__"

    def create(self, validated_data):
        # print(validated_data)
        children_data = validated_data.pop('children', None)
        interests_data = validated_data.pop('interests', None)
        service_cost_data = validated_data.pop('service_cost', None) 

        item = InfluencersDetail.objects.create(**validated_data)
        item.save()
        
        children = []
        if children_data is not None:
            for child in children_data:
                child['influencer'] = item
                child_data = InfluencersChildren.objects.create(**child)
                child_data.save()
                children.append(child_data)
                item.children.add(*children)
        
        interests = []
        if interests_data is not None:
            for interest in interests_data:
                interest_d = InfluencersInterests.objects.create(**interest)
                interest_d.save()
                interests.append(interest_d)
                item.interests.add(*interests)

        service_cost = []
        if service_cost_data is not None:
            for cost_data in service_cost_data:
                service_cost_d = InfluencersServicesCost.objects.create(**cost_data)
                service_cost_d.save()
                service_cost.append(service_cost_d)
                item.service_cost.add(*service_cost)

        return item

    def update(self, instance, validated_data):
        instance.influencer_name = validated_data.pop('influencer_name', instance.influencer_name)
        instance.insta_username = validated_data.pop('insta_username', instance.insta_username)
        instance.gender = validated_data.pop('gender', instance.gender)
        instance.about_influencer = validated_data.pop('about_influencer', instance.about_influencer)
        instance.no_of_posts = validated_data.pop('no_of_posts', instance.no_of_posts)
        instance.no_of_likes = validated_data.pop('no_of_likes', instance.no_of_likes)
        instance.no_of_comments = validated_data.pop('no_of_comments', instance.no_of_comments)
        instance.no_of_impressions = validated_data.pop('no_of_impressions', instance.no_of_impressions)
        instance.no_of_reach = validated_data.pop('no_of_reach', instance.no_of_reach)
        instance.no_of_children = validated_data.pop('no_of_children', instance.no_of_children)
        instance.avatar = validated_data.pop('avatar', instance.avatar)
        instance.save()
        return instance


class GetInfluencersDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencersDetail
        fields = "__all__"
        depth = 1