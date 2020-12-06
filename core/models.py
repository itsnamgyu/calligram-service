from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Result(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    image = models.ImageField()
    text = models.TextField()
    corrected_text = models.TextField()
    correction_info = models.TextField(null=True)
    correct = models.BooleanField()
