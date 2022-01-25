from django.http import HttpResponse


def posts_index(request):
    return HttpResponse("Posts index view")