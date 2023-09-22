from .serializers import NewsSerializer
from .models import NewsModel
from rest_framework import generics
from .permissions import StaffPermission, AdminPermission
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerPermission

class ListAPiView(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermission, OwnerPermission)

class CreateAPiView(generics.CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermission, OwnerPermission)

class UpdateStatusApiView(generics.UpdateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermission, OwnerPermission, AdminPermission)

class DestroyApiView(generics.DestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermission, OwnerPermission)

class AllCommandsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermission, OwnerPermission)

