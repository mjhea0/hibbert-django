from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	likes_cheese = models.BooleanField()
	favorite_hamster_name = models.CharField(max_length=50)

# if object exists grab it, else create it
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


