from rest_framework import status, viewsets
from rest_framework.response import Response
from influencers.models import (
    InfluencersDetail,
    InfluencersChildren,
    InfluencersCategories
)
from influencers.serializers import (
    InfluencersDetailSerializer,
    GetInfluencersDetailSerializer,
    InfluencersCategoriesSerializer
)
from rest_framework.parsers import (JSONParser, MultiPartParser, FormParser, FileUploadParser)
from rest_framework.permissions import IsAuthenticated, AllowAny


class InfluencersDetailViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = InfluencersDetail.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = GetInfluencersDetailSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = InfluencersDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"influencer profile created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = InfluencersDetailSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"influencer profile updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = GetInfluencersDetailSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_queryset(request).get(pk=pk).delete()
        return Response({"data":[], "success":True, "message":"influencer profile deleted successfully"}, status=status.HTTP_200_OK)


class InfluencersCategoriesViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = InfluencersCategories.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = InfluencersCategoriesSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
        serializer = InfluencersCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"influencer category created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = InfluencersCategoriesSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"influencer category updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = InfluencersCategoriesSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_queryset(request).get(pk=pk).delete()
        return Response({"data":[], "success":True, "message":"influencer category deleted successfully"}, status=status.HTTP_200_OK)