from django.db import models

class User(models.Model):
    id_secuencial = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    geo_state = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
