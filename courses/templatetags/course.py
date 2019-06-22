from django import template

register = template.Library()


@register.filter
def model_name(obj):
    """
    Retrieves the 'model_name' for an object
    (here for content-type), otherwise raises error.
    """
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
