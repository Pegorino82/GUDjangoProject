from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user
from django.db.utils import IntegrityError
import datetime

from authapp.models import AuthApp
from customers.models import Customer


def login_view(request):
    # TODO проверить, есть ли зарегистрированный пользователь
    # TODO если есть, то сначала сделать отметку в бд о его выходе
    success_url = reverse_lazy('customersapp:customer')
    next = request.GET.get('next') if 'next' in request.GET.keys() else ''  # TODO
    notification = {'next': next}  # TODO
    if request.method == 'POST':
        usr_name = request.POST.get('username')
        psw = request.POST.get('password')
        # if request.POST.get('login'):
        user = authenticate(username=usr_name, password=psw)
        if user and user.is_active:
            auth_act = AuthApp.objects.create(user=user)
            auth_act.login = datetime.datetime.now()
            auth_act.save()
            login(request, user)
            if 'next' in request.POST.keys():  # TODO
                return redirect(request.POST['next'])  # TODO
            else:  # TODO
                return redirect(success_url)  # TODO
        else:
            notification.update(
                {
                    'user_name': usr_name,
                    'warn': 'incorrect username or password'
                }
            )
    return render(request, 'authapp/login.html', notification)


def logup_view(request):
    success_url = reverse_lazy('customersapp:customer')
    notification = {}
    if request.POST.get('logup'):
        usr_name = request.POST.get('username')
        psw = request.POST.get('password')
        avatar = request.FILES.get('avatar')
        checker = get_user(request)
        if checker.is_anonymous:
            try:
                customer = Customer(
                    username=usr_name,
                    _avatar=avatar
                )
                customer.is_active = True
                customer.set_password(psw)
                customer.save()

                notification = {
                    'user_name': usr_name,
                    'warn': 'Congratulations!'
                }
            except IntegrityError:
                notification = {
                    'user_name': usr_name,
                    'warn': 'Name is occupied! Choose another'
                }

            else:
                user = authenticate(username=usr_name, password=psw)

                if user and user.is_active:
                    auth_act = AuthApp.objects.create(user=user)
                    auth_act.logup = datetime.datetime.now()
                    auth_act.save()
                    login(request, user)
                    return redirect(success_url)

    return render(request, 'authapp/logup.html', notification)


def logout_view(request, **kwargs):
    success_url = reverse_lazy('customersapp:customer')
    notification = {}
    user = request.user
    # if request.POST.get('exit'):
    auth_act = AuthApp.objects.create(user=user)
    auth_act.logout = datetime.datetime.now()
    auth_act.save()
    logout(request)
    return redirect(success_url)
    # return render(request, 'authapp/logout.html', notification)
