from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Result(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    image = models.ImageField()
    text = models.TextField(null=True, blank=False)
    corrected_text = models.TextField(null=True, blank=False)
    correction_info = models.TextField(null=True, blank=False)
    correct = models.BooleanField(null=True, blank=False)
