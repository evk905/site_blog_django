from django import template
import publications.views as views
from publications.models import Category, Tag

register = template.Library()


# @register.inclusion_tag('publications/list_categories.html')
# def show_categories(cat_selected=0):
#     cats = Category.objects.all()
#     return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('publications/list_tags.html')
def show_all_tags():
    return {'tags': Tag.objects.all()}