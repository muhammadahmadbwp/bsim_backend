from rest_framework import status, viewsets
from rest_framework.response import Response
from adminpanel.models import (
    BrandCategory,
    BrandDetail,
    CampaignDetail,
    CampaignDates,
    HashtagDetail
)
from adminpanel.serializers import (
    BrandCategorySerializer,
    BrandDetailSerializer,
    CampaignDetailSerializer,
    CampaignDatesSerializer,
    HashtagDetailSerializer
)
from rest_framework.parsers import (JSONParser, MultiPartParser, FormParser, FileUploadParser)
from rest_framework.permissions import IsAuthenticated, AllowAny


class BrandCategoryViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = BrandCategory.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = BrandCategorySerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BrandCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"brand category created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = BrandCategorySerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"brand category updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = BrandCategorySerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_queryset(request).get(pk=pk).delete()
        return Response({"data":[], "success":True, "message":"brand category deleted successfully"}, status=status.HTTP_200_OK)


class BrandDetailViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = BrandDetail.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = BrandDetailSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
        serializer = BrandDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"brand detail created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = BrandDetailSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"brand detail updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = BrandDetailSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_queryset(request).get(pk=pk).delete()
        return Response({"data":[], "success":True, "message":"brand detail deleted successfully"}, status=status.HTTP_200_OK)


class HashtagDetailViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = HashtagDetail.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = HashtagDetailSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = HashtagDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"hashtag detail created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = HashtagDetailSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"hashtag detail updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = HashtagDetailSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_queryset(request).get(pk=pk).delete()
        return Response({"data":[], "success":True, "message":"hashtag detail deleted successfully"}, status=status.HTTP_200_OK)


class CampaignDetailViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = CampaignDetail.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = CampaignDetailSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CampaignDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"campaign detail created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = CampaignDetailSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"campaign detail updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset(request).get(pk=pk)
        serializer = CampaignDetailSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_queryset(request).get(pk=pk).delete()
        return Response({"data":[], "success":True, "message":"campaign detail deleted successfully"}, status=status.HTTP_200_OK)