from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def check_image(self):
    set_height = 28
    set_width = 28

    try:
        height = self.image.height
        width = self.image.width

        # JPG etc. seems to work but for now we require png
        if self.image.format not in ('PNG'):
            raise ValidationError(
                "Unsupported image type. Please upload a PNG file.")

        # Validate dimensions (28x28 for now, we could also resize etc.)
        if width != set_width or height != set_height:
            raise ValidationError(
                f"Image dimensions must be {set_width}x{set_height}px. "
                f"Current dimensions are {width}x{height}px.")

    except Exception as e:
        raise ValidationError(f"Invalid image file: {e}")

    return self.image

class Image(models.Model):
    image = models.ImageField(
        _("Image"), validators=[check_image])
