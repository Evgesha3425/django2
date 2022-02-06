import logging

from django.contrib.auth.models import User
from django.http import HttpResponse

from posts.models import Post

logger = logging.getLogger(__name__)


def posts_index(request):
    result = ""
    for post in Post.objects.filter(title="Test2"):
        result += f"<div style='border: 1px solid black'>"
        result += f"<h1>{post.title}</h1>"
        result += f"<div>{post.text}</div>"
        result += f"</div>"
    return HttpResponse(result)


