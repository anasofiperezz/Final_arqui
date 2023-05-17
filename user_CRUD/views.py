from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


class Signup(View):

    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, 'user/signup.html', context)

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                context = {'form': UserCreationForm,
                           'error': 'Username already exists'}
                return render(request, 'user/signup.html', context)
        context2 = {'form': UserCreationForm,
                    'error': 'Password Miss-Match'}
        return render(request, 'user/signup.html', context2)


class Signout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class Signin(View):
    def get(self, request):
        context = {'form': AuthenticationForm}
        return render(request, 'user/signin.html', context)

    def post(self, request):
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {'form': AuthenticationForm,
                       'error': 'Username or Password incorrect'}
            return render(request, 'user/signin.html', context)
        else:
            login(request, user)
            return redirect('index')
