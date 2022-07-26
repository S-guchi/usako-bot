from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Spaceにパスワードつける
class Space(models.Model):

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "space"


class UserManager(BaseUserManager):
    def create_user(self, line_id, nickname, space=None, password=None):

        if not line_id:
            raise ValueError("Users must have an line id")

        user = self.model(
            line_id=line_id,
            nickname=nickname,
            space=space,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, line_id, nickname, space=None, password=None):
        user = self.create_user(
            line_id=line_id,
            nickname=nickname,
            space=space,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    line_id = models.CharField(max_length=128, unique=True)
    nickname = models.CharField(max_length=128)
    space = models.ForeignKey(
        Space, db_column="space_id", on_delete=models.CASCADE, null=True
    )

    password = None
    last_login = None

    objects = UserManager()
    USERNAME_FIELD = "line_id"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self) -> str:
        return self.nickname

    class Meta:
        db_table = "user"
