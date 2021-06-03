from django import template
from django.db.models import Count
from post.models import Post


register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)

#
# @register.simple_tag
# def total_posts():
#     return Post.published.count()
#
#
@register.inclusion_tag('includes/latest_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.all().order_by('-created_date')[:count]
    return {'latest_posts': latest_posts}

#
# @register.simple_tag
# def get_most_commented_posts(count=5):
#     return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
#
