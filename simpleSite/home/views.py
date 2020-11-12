from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    name = request.user.username

    return render(request, 'home/homehtml.html')


@login_required
def logout_func(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('welkom:welkom'))