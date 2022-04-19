from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


class UserBase(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_superuser=True status')
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True status')
        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError("You must enter a valid email address")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserManager(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserBase()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'user_name'

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"