from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from . models import *

#This is the asset serializer for asset genre.
class AssetSerializer(ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'
        extra_kwargs = {'company': {'read_only': True}}

#To ensure that, once company is not going to see the available devices of another company
class AssetForeignKeyuser(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        return AssetType.objects.filter(company=user)

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {'company': {'read_only': True}}

#This intermediate serializer does the same as the previous intermediate serializer. It just applies for available employees. 
class ForeignKeyemployee(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Employee.objects.filter(company=self.context['request'].user)

class GivenAssetSerializer(ModelSerializer):
    asset = AssetForeignKeyuser()
    given_to = ForeignKeyemployee()
    class Meta:
        model = GivenAsset
        fields = ['asset', 'given_to', 'given_asset_status', 'asset_given_at', 'returned_asset_status', 'asset_returned_at']
        
#Default create overriding.
    def create(self, validated_data):
        user = self.context['request'].user
        if user is not None and user.is_authenticated:
            givenasset = GivenAsset.objects.create(
                given_asset_status = validated_data['given_asset_status'],
                asset_given_at = validated_data['asset_given_at'],
                returned_asset_status = validated_data['returned_asset_status'],
                asset_returned_at = validated_data['asset_returned_at'],
                asset = validated_data['asset'],
                given_to = validated_data['given_to']
            )
            givenasset.save()
            return givenasset
        else:
            raise serializers.ValidationError('Not authenticated')