import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    """
    user manager
    """

    def create_user(self, username, password=None):
        user = self.model(username=username, password=password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def check_password_valid(self, pwd1, pwd2):
        if pwd1 != pwd2:
            return False
        return True


class User(AbstractBaseUser):
    """
    base user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=64, unique=True, db_index=True, verbose_name='账号')
    password = models.CharField(
        max_length=64, db_index=True, verbose_name='密码')
    email = models.EmailField(
        max_length=255, null=True, blank=True, verbose_name='邮箱')
    # first_name = models.CharField(max_length=64, null=True)
    # last_name = models.CharField(max_length=64, null=True)
    nickname = models.CharField(max_length=64, null=True, verbose_name='昵称')
    head_img = models.ImageField(
        upload_to='upload/' + str(uuid.uuid4()) + '/',
        null=True,
        blank=True,
        verbose_name='头像')
    telephone = models.CharField(
        max_length=11, null=True, blank=True, verbose_name='电话')
    sex = models.CharField(max_length=2, null=True, verbose_name='性别')
    # is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    is_superuser = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # user_permissions = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
