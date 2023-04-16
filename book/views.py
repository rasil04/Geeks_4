from django.shortcuts import render
from . import models

def bookview(request):
    post = models.Book.objects.all()
    context = {
        'post_object': post
    }
    return render(request, 'book.html', context)