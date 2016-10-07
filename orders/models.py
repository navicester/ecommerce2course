from django.conf import settings
from django.db import models

# Create your models here.
class UserCheckout(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
	email = models.EmailField(unique=True) #--> required

	def __unicode__(self): #def __str__(self):
		return self.email	