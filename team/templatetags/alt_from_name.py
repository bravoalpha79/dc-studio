from django import template

register = template.Library()

@register.filter(name="alt_from_name")
def img_alttext(name):
    """ extract name (for photo alt text) from name_and_title """
    if "." not in name:
        return ""
    return name.split(",")[0].split(".")[-1].strip()

