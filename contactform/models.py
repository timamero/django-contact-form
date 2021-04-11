from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now


class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField(blank=True)
    date = models.DateField(default=now)
    message = models.TextField()

    def __str__(self):
        return f'{self.last_name}, {self.first_name} ({self.date})'

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])
