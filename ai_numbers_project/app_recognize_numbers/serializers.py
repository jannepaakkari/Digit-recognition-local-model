from rest_framework import serializers
from django.core.exceptions import ValidationError
from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ("id", "image")
