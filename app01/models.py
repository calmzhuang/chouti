from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32, db_index=True)
    telephone = models.CharField(max_length=32, unique=True)
    pwd = models.CharField(max_length=64)
    cTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = [
            ('username', 'pwd')
        ]

        unique_together = [
            ('username', 'pwd')
        ]

class TelCode(models.Model):
    telephone = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=64)
    times = models.IntegerField(max_length=1)
    cTime = models.DateTimeField(auto_now_add=True)