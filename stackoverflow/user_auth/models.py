from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=20)
    user_create_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_name