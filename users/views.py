from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView


def user_template(request, user_id):

    context = {
        'links':  {
            'Люди': '/',
            'Интересные публикации': '/',
            'Сообщества': '/',
        },
    }

    user = User.objects.get(id=user_id)
    name = f'{user.first_name} {user.last_name}'

    return render(request, 'user.html', {'context': context, 'name': name, 'user_id': user_id})
