from django.db import models
from django.contrib.auth.models import User


condition_before = [
    ['1', 'Unused'],
    ['2', 'Used'],
    ['3', 'New']
]

#Secondary asset conditions are summerized here

condition_after = [
    ['1', 'Unused'],
    ['2', 'Used'],
    ['3', 'Out of date'],
    ['4', 'Damaged'],
    ['5', 'In use'],
    ['6', 'New'],
    ['7', 'lost'],
    ['8', 'stolen']
]

class AssetType(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, null = True) #admin or user
    name = models.CharField(max_length=50, null=True, blank=False) #asset type
    
    # here meta class is used to prevent different company to update one asset more than one
    class Meta:
        constraints = [models.UniqueConstraint(fields=['company', 'name'], name = 'unique')]
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.IntegerField(null=True, blank=False, unique=True)
    #ID number must be unique.
    employee_name = models.CharField(max_length=100, blank=False)
    company = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return str(self.employee_id)
    
class GivenAsset(models.Model):
    asset = models.ForeignKey(AssetType, on_delete=models.CASCADE, null = True)
    given_to = models.ForeignKey(Employee, on_delete=models.CASCADE, null = True)
    given_asset_status = models.CharField(max_length=20, choices=condition_before, default='3')
    asset_given_at = models.DateField(null=True, blank=True)
    returned_asset_status = models.CharField(max_length=20, choices=condition_after, default='6')
    asset_returned_at = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.asset