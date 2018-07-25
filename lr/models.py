from django.db import models
from django.forms import ModelForm

# Create your models here.

class Landlord(models.Model):
    landlord_id = models.CharField(max_length = 9, primary_key = True)
    landlord_first_name = models.CharField(max_length = 64)
    landlord_last_name = models.CharField(max_length = 64)


class Apartment(models.Model):
    apartment_id = models.IntegerField(primary_key = True)
    street_name = models.CharField(max_length = 64)
    street_number = models.PositiveSmallIntegerField()
    apartment_number = models.PositiveSmallIntegerField()
    city = models.CharField(max_length = 64)


class Tenent(models.Model):
    tenent_id = models.CharField(max_length = 9, primary_key = True)
    tenent_first_name = models.CharField(max_length = 64)
    tenent_last_name = models.CharField(max_length = 64)


class Review(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete = models.CASCADE)
    tenent = models.ForeignKey(Tenent, on_delete = models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete = models.CASCADE)

    summary = models.CharField(max_length = 70)
    maintanance_description = models.TextField(max_length = 256)
    maintanance_rating = models.PositiveSmallIntegerField()
    contract_description = models.TextField(max_length = 256)
    contract_rating = models.PositiveSmallIntegerField()
    contact_start = models.DateField()
    contract_end = models.DateField(null=True)
    is_contract_ended = models.BooleanField()
    rent_rate_monthly = models.SmallIntegerField(null=True)
    class Meta:
        unique_together = (("landlord", "tenent", "apartment"),)
    
    def __str__(self):
        return self.summary


class TenentForm(ModelForm):
    class Meta:
        model = Tenent
        fields = ['tenent_id', 'tenent_first_name', 'tenent_last_name']
