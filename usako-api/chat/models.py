from django.db import models
from config.models import Space


class Chat(models.Model):

    talk = models.CharField(max_length=256)
    space = models.ForeignKey(
        Space, db_column="space_id", on_delete=models.CASCADE, null=True
    )

    def __str__(self) -> str:
        return self.talk

    class Meta:
        db_table = "chat"
