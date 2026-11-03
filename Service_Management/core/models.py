from django.db import models

class Services(models.Model):
    service_name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    duration=models.DurationField()
    STATUS_CHOICES=[('PENDING','Pending'),
                     ('IN_PROGRESS','In-Progress'),
                     ('COMPLETED','Completed')]
    status=models.CharField(choices=STATUS_CHOICES,max_length=30, default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.service_name


