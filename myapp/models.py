from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, email, account_id, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, account_id=account_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, account_id, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, account_id, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )


class CustomUser(AbstractUser):
    userID = models.CharField("ID", max_length=50)
    objects = UserManager()

    def __str__(self):
        return self.userID


class Todo(models.Model):
    title = models.CharField("Name", max_length=50)
    description = models.TextField("ex", blank=True)
    deadline = models.DateField("Deadline")
    user_name = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
