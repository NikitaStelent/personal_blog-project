from django import template
from .category_translation import CATEGORY_TRANSLATIONS

register = template.Library()


@register.filter
def translate_category(category):
    return CATEGORY_TRANSLATIONS.get(str(category), str(category))
