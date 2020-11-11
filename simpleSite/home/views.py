from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    name = request.user.username

    return HttpResponse("Hi %s" %(name))