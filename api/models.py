from django.db import models

class ApiVersion(models.Model):
    version = models.CharField(max_length=10) 
    description = models.TextField()  

    def __str__(self):
        return self.version

