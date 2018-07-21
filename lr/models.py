from django.db import models

# Create your models here.

class Review(models.Model):
    landlord_id = models.CharField(max_length = 9)
    tenent_id = models.CharField(max_length = 9)
    apartment_id = models.IntegerField()

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
        unique_together = (("landlord_id", "tenent_id", "apartment_id"),)
    
    def __str__(self):
        return self.summary


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


class tenent(models.Model):
    tenent_id = models.CharField(max_length = 9, primary_key = True)
    tenent_first_name = models.CharField(max_length = 64)
    tenent_last_name = models.CharField(max_length = 64)
