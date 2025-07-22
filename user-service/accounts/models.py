# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models

# CustomUser model extending AbstractUser
# with additional fields if needed
class CustomUser(AbstractUser):
    pass  # extend with more fields if needed
