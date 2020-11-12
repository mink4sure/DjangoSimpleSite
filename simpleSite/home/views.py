from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User, Group


@login_required
def home(request):
    name = request.user.username
    user = User.objects.get(username=name)


    return render(request, 'home/homehtml.html')


@login_required
def logout_func(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('welkom:welkom'))