from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from createPosts.models import Posts
from authorization.models import Profile


def user_template(request, user_id):
    context = {
        'links': {
            'Люди': '/',
            'Интересные публикации': '/',
            'Сообщества': '/',
        },
    }

    post_dict = {}

    user = User.objects.get(id=user_id)
    profile = Profile.objects.get()
    post = None

    try:
        post = Posts.objects.filter(user_id=profile.user_id)
    except Posts.DoesNotExist:
        print('Нет постов')

    print(post_dict)

    try:
        if request.session['sessionID']:
            name = f'{user.first_name} {user.last_name}'
            return render(request, 'user.html',
                          {'context': context, 'name': name, 'user_id': user_id, 'user_post_dict': post})
    except:
        return redirect(to='/')


def logout_user(request):
    logout(request)
    return redirect(to='/')
