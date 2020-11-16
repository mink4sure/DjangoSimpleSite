from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import FriendGroup
from .forms import UploadFileForm


# Function for saving files; needs to be based elsewhere in the final version
def save(f):
    return f.ch


@login_required
def home(request):
    name = request.user.username
    user = User.objects.get(username=name)


    return render(request, 'home/homehtml.html')


@login_required
def logout_func(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('welkom:welkom'))

@login_required
def create_group(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)

        friend_group_name = request.POST.get('friend_group_name')
        friend_group = FriendGroup(name=friend_group_name)

        friend_group.user_set.add(user)
        friend_group.save()

        return HttpResponseRedirect("/home/")


    return render(request, 'home/create_group.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

