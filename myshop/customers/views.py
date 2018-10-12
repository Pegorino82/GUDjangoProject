from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from .models import Customer


def login_view(request):
    print(request.POST)
    notification = {}
    if request.method == 'POST':
        usr_name = request.POST.get('username')
        psw = request.POST.get('password')

        if request.POST.get('login'):

            user = authenticate(username=usr_name, password=psw)

            if user and user.is_active:
                login(request, user)

            else:
                notification = {
                    'user_name': usr_name,
                    'warn': 'incorrect username or pasword'
                }

        if request.POST.get('exit'):
            logout(request)

        if request.POST.get('logup'):

            checker = Customer.objects.get(username=usr_name)
            if not checker:

                customer = Customer(
                    username=usr_name
                )
                customer.is_active = True
                customer.set_password(psw)
                customer.save()

                notification = {
                    'user_name': usr_name,
                    'warn': 'Congratulations!'
                }
            else:
                notification = {
                    'user_name': usr_name,
                    'warn': 'Name is occupied! Choose another'
                }

    return render(request, 'customers/customer.html', notification)


def logout_view(request):
    pass

    print(request.POST)
    notification = {}

    if request.POST.get('exit'):
        pass

    return render(request, 'customers/customer.html', notification)
