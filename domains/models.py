from django.db import models

# Create your models here.
class Domain(models.Model):
    STATUS_CHOICE=[
        ('pending','Pending'),
        ('verified','Verified'),
        ('rejected','Rejected'),
    ]
    domain=models.CharField(max_length=50, unique=True)
    isActive=models.BooleanField(default=True)
    status=models.CharField(choices=STATUS_CHOICE, max_length=10, default="pending",)
    createdDate=models.DateTimeField(auto_now_add=True)