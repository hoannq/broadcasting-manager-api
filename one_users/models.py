from __future__ import unicode_literals
from datetime import datetime, time
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


class OneUserManager(BaseUserManager):
    def _create_user(self, email, password, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        now = datetime.now()
        if email is None:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)

        user = self.model(email=email,
                          is_superuser=is_superuser,
                          is_active=is_active,
                          date_joined=now,
                          **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: regular user
        """
        return self._create_user(email, password, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: admin user
        """
        return self._create_user(email, password, True,
                                 **extra_fields)


class AbstractOneUsers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=255, blank=True, default="")
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=0)

    class Meta:
        db_table = "x_users"
        abstract = True

    objects = OneUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def __unicode__(self):  # __unicode__ on Python 2
        return self.username


class OneUsers(AbstractOneUsers):
    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    class Meta(AbstractOneUsers.Meta):
        swappable = 'AUTH_USER_MODEL'
