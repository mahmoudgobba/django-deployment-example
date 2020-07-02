from django import template

register = template.Library()
@register.filter(name='cut')
def Cut(value,arg):
    """
    This cuts out all value of "arg" from the string
    """

    return value.replace(arg,'')

# register.filtter('cut',Cut)
