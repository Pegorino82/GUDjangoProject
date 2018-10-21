from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user
from django.db.utils import IntegrityError

from customers.models import Customer
from customers.forms import CustomerModelForm


def create_customer(request):
    template_name = 'customers/create_customer.html'
    success_url = reverse_lazy('customersapp:list_customer')
    form = CustomerModelForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect(success_url)
    return render(request, template_name, {'form': form})


def update_customer(request, **kwargs):
    template_name = 'customers/update_customer.html'
    success_url = reverse_lazy('customersapp:list_customer')
    pk = kwargs.get('pk')
    obj = Customer.objects.get(pk=pk)
    # TODO сделать автозаполнение DateInput данными из модели

    form = CustomerModelForm(instance=obj)

    if request.method == 'POST':
        form = CustomerModelForm(
            request.POST,
            request.FILES,
            instance=obj
        )
        if form.is_valid:
            form.save()
            return redirect(success_url)
    return render(request, template_name, {'form': form})


def detail_customer(request, **kwargs):
    template_name = 'customers/detail_customer.html'
    pk = kwargs.get('pk')
    obj = Customer.objects.get(pk=pk)

    return render(request, template_name, {'object': obj})


def list_customer(request):
    template_name = 'customers/list_customer.html'
    results = Customer.objects.all()

    return render(request, template_name, {'results': results})

def delete_customer(request, **kwargs):
    template_name = 'customers/delete_customer.html'
    success_url = reverse_lazy('customersapp:list_customer')
    pk = kwargs.get('pk')
    obj = Customer.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect(success_url)
    return render(request, template_name, {'object': obj})


def login_view(request):
    notification = {}
    if request.method == 'POST':
        usr_name = request.POST.get('username')
        psw = request.POST.get('password')
        # avatar = request.POST.get('avatar')

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
            avatar = request.FILES.get('avatar')
            print('-->', request.FILES)

            checker = get_user(request)

            if checker.is_anonymous:

                try:
                    customer = Customer(
                        username=usr_name,
                        avatar=avatar
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
                        login(request, user)

    return render(request, 'customers/customer.html', notification)
