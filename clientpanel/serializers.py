from rest_framework import serializers
from clientpanel.models import (
    ClientsDetail,
)


class ClientsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientsDetail
        fields = "__all__"