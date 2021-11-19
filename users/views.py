from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout


def user_template(request, user_id):
    context = {
        'links': {
            'Люди': '/',
            'Интересные публикации': '/',
            'Сообщества': '/',
        },
    }

    user = User.objects.get(id=user_id)

    try:
        if request.session['sessionID']:
            name = f'{user.first_name} {user.last_name}'
            return render(request, 'user.html', {'context': context, 'name': name, 'user_id': user_id})
    except:
        return redirect(to='http://localhost:8000/')


def logout_user(request):
    logout(request)
    return redirect(to='http://localhost:8000')
