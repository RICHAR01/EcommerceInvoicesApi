from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    cd = models.DateTimeField(auto_now_add=True)
    md = models.DateTimeField(auto_now=True)
    cu = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
