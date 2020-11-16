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


# The home screen of a user
@login_required
def home(request):
    name = request.user.username
    user = User.objects.get(username=name)

    return render(request, 'home/homehtml.html')


# Login out a user using the default logout function of django
@login_required
def logout_func(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('welkom:welkom'))


# The view for creating a new friend group
@login_required
def create_group(request):
    if request.method == 'POST':
        # getting the user that makes a new group
        user = User.objects.get(username=request.user.username)

        # Getting the name from the form and making a group with the corresponding name
        friend_group_name = request.POST.get('friend_group_name')
        friend_group = FriendGroup(name=friend_group_name)

        # Adding the current user to the group and saving the group
        friend_group.user_set.add(user)
        friend_group.save()

        # Redirecting to the users home page
        return HttpResponseRedirect("/home/")

    # Loading the create group view
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

