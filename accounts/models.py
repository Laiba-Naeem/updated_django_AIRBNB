# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .manager import UserManager

# # Create your models here.


# class User(AbstractUser):

#     username = None
#     name = models.CharField(max_length=80, null=True, blank=True)
#     email = models.EmailField(unique=True)
#     mobile = models.CharField(max_length=15, null=True)
#     is_verified = models.BooleanField(default=False)
#     email_token = models.CharField(max_length=100, null=True, blank=True)
#     forget_password = models.CharField(max_length=100, null=True, blank=True)
#     last_login_time = models.DateTimeField(null=True, blank=True)
#     last_logout_time = models.DateTimeField(null=True, blank=True)

#     objects = UserManager()
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["is_verified", "email_token"]


# class GoogleSignUser(AbstractUser):
#     name = models.CharField(max_length=80, null=True, blank=True)
#     email = models.EmailField(unique=True)


from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, null=True)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["is_verified", "email_token"]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_custom',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class GoogleSignUser(AbstractUser):
    name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='googlesignuser_set_custom',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='googlesignuser_set_custom',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
