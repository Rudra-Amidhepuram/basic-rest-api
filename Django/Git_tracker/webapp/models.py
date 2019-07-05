from django.db import models
#from django.contrib.auth.models import AbstractUser

class user(models.Model):

	name=models.CharField(max_length=200)
	p_name=models.CharField(max_length=50)
	mobile= models.IntegerField()


