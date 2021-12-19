from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Posts
from services.generate_id import generate_random_num
import datetime


def postCreator(request):
    if request.method == 'POST':
        print(True)
        data_post = request.POST.get('comment')
        posts = Posts(id=generate_random_num(), post=data_post, post_date=datetime.datetime.now(), user_id=8821876, user_login='thomas95')
        posts.save()
        return HttpResponse('Hello World')
