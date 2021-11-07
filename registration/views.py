from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from services.forms import RegisterUserForm
from services.registration import registration
from django.contrib.auth import login
from werkzeug.security import generate_password_hash


class RegisterUser(CreateView):
    template_name = 'reg.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        return dict(list(context.items()))

    def dispatch(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if request.method == 'POST':
            name = f'{form.data["first_name"]} {form.data["last_name"]}'
            user_login = form.data['username']
            email = form.data['email']
            password = form.data['password1']

            registration(name, user_login, email, generate_password_hash(password))
            user = User.objects.create_user(username=user_login, email=email, first_name=form.data["first_name"],
                                            last_name=form.data["last_name"], password=password)
            user.save()
            user_id = user.id
            login(request, user)

            return redirect(f'http://localhost:8000/users/{user_id}')

        return render(request, 'reg.html', {'form': RegisterUserForm})
