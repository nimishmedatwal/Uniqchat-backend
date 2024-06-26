from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, uuid, public_key, private_key, **extra_fields):
        user = self.model(uuid=uuid, public_key=public_key, **extra_fields)
        user.set_password(private_key)  # storing private key as hashed password (not recommended for actual private key storage)
        user.save(using=self._db)
        return user

    def create_superuser(self, uuid, public_key, private_key, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(uuid, public_key, private_key, **extra_fields)

class User(AbstractBaseUser):
    uuid = models.CharField(max_length=64, unique=True)
    public_key = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'uuid'
    REQUIRED_FIELDS = ['public_key']
