from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from demo.forms import login as login_form


def login(request):
    """
    login
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'GET' and 'next' in request.GET:
        next_page = request.GET['next']
    else:
        next_page = '/'

    if request.method == "POST":
        form = login_form.LoginForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(request.POST.get('next', '/'))
    else:
        form = login_form.LoginForm(request)

    kwargs = {
        'form': form,
        'next': next_page,
    }

    return render(request, 'login.html', kwargs)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def register(request):
    return render(request, 'register.html')
