from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from django.contrib.auth.models import User

def welkom(request):
    template = loader.get_template('welkom/welkomhtml.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('welkom/register.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def AddUser(request):
    name = request.POST['your_name']
    password = request.POST['password']
    check_name_exsists = User.objects.filter(username=name)
    if check_name_exsists:
        return render(request, 'welkom/register.html',
                      {'error_message': "This name is already used"})
    else:
        user = User(username=name)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(reverse('welkom:welkom'))




def login(request):
    template = loader.get_template('welkom/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
