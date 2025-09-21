from django.db import models

# Create your models here.
class Domain(models.Model):
    STATUS_CHOICE=[
        (1 ,'Pending'),
        (2 ,'Verified'),
        (3 ,'Rejected'),
    ]
    domain=models.CharField(max_length=50, unique=True)
    isActive=models.BooleanField(default=True)
    status=models.IntegerField(choices=STATUS_CHOICE, default=1,)
    createdDate=models.DateTimeField(auto_now_add=True)