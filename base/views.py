from . models import *
from knox.auth import TokenAuthentication
from . serializers import *
from rest_framework import generics, filters, permissions

#Available asset view.
class Assets(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return AssetType.objects.filter(company=user)
    
    def perform_create(self, serializer):
        serializer.save(company = self.request.user)

class Asset(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer

    def get_queryset(self):
        user = self.request.user
        return AssetType.objects.filter(company=user)

    def perform_update(self, serializer):
        serializer.save(company = self.request.user)

#Available employe view.
class Employee(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company=user)

    def perform_create(self, serializer):
        serializer.save(company = self.request.user)

class Employees(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company=user)
    
    def perform_update(self, serializer):
        serializer.save(company = self.request.user)
        
#Given asset view.  
class GivenAssets(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions .IsAuthenticated]
    #search funcionality based upon employee_id
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['given_to__employee_id',]
    serializer_class = GivenAssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return GivenAsset.objects.filter(given_to__company=user)
    
class GivenAsset(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GivenAssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return GivenAsset.objects.filter(given_to__company=user)