from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.username

