from django.db import models
from model_utils.models import TimeStampedModel

class ContactDetails(TimeStampedModel):
    contact_name = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    contact_message = models.CharField(max_length=255, blank=True, null=True)