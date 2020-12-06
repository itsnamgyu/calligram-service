from django import forms

from core.models import *


class ImageForm(forms.Form):
    image = forms.ImageField()
