import random
from random import choice
from werkzeug.security import generate_password_hash
from authorization.models import Users, Profile
from django.contrib.auth.models import User


def generate_random_num():
    random_num = ''
    random_list = list('123456789')
    for i in range(random.randint(3, 9)):
        random_num += choice(random_list)

    return random_num


def registration(name, user_login, email, password):
    id = generate_random_num()
    user_hash_pass = generate_password_hash(password)
    user = Users(userID=id, user_name=name, user_login=user_login, email=email, password=user_hash_pass)
    profile = Profile(user_id=id, id=generate_random_num(), user_login=user_login)
    profile.save()
    user.save()

    # user_create = user.objects.create(username=user_login, password=user_hash_pass)
    # user_create.save()
