from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone






class User(AbstractUser):

	special = models.DateTimeField(default = timezone.now  , verbose_name='special until ' )
	 


	def is_special_user(self):

		if self.special > timezone.now():
			return True

		else:
			return False
	is_special_user.boolean = True
	is_special_user.short_description = 'special user'
