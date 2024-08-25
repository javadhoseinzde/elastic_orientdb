from django.db import models

# Create your models here.

class OrientHost(models.Model):
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.port + " " + self.password