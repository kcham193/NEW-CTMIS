# your_app_name/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, ADMINS):
    return user.groups.filter(name=ADMINS).exists()
