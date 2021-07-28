from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def upload_to(instance, filename):
    return './media/{filename}'.format(filename=filename.strip("/"))


def check_image(self):
    set_height = 28
    set_width = 28
    height = self.image.height
    width = self.image.width

    # JPG etc. seems to work but for now we require png
    if self.image.format not in ('PNG'):
        raise ValidationError(
            "Unsupported image type. Please upload png file")

    if width != set_width or height != set_height:
        raise ValidationError("Height and Width needs to be 28px")
    return self.image


class Image(models.Model):
    image = models.ImageField(
        _("Image"), upload_to=upload_to, validators=[check_image])
