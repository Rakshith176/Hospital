from django.db import models

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    specification = models.TextField()
    contact = models.IntegerField()
    is_doctor = models.BooleanField(default=False)

     def __str__(self):
      return self.user.username
