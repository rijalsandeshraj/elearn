from django.core.exceptions import ValidationError


def validate_image_size(image):
    """
    Raises Validation Error if the image size is greater than 10 MB.
    """
    image_size = image.size
    limit_in_mb = 10
    if image_size > limit_in_mb * 1024 * 1024:
        raise ValidationError("Image must be less than " +
                              str(limit_in_mb) + " MB.")
    return image
