from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class subrequest(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100) 
    email = models.EmailField()
    service_type = models.CharField(max_length=100)
    details = models.TextField()
    
    def __str__(self):
        return self.fname

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    )

    customer_name = models.CharField(max_length=100)
    request_details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer_name}'s ServiceRequest"
    
###########################################
class Profile(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user.username} Profile'