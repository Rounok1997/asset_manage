from django.urls import path
from . views import *

urlpatterns = [
    path('asset/', Assets.as_view(), name='ListOfAssets'),
    path('asset/<int:pk>', Asset.as_view(), name='IndividualAsset'),
    
    path('employee/', Employees.as_view(), name='ListOfEmployees'),
    path('employee/<int:pk>', Employee.as_view(), name='IndividualEmployee'),
    
    path('given_asset/', GivenAssets.as_view(), name='AssetsGiven'),
    path('given_asset/<int:pk>', GivenAsset.as_view(), name='AssetDetail'),
]