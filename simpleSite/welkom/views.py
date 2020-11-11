from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as auth

from django.contrib.auth.models import User

def welkom(request):
    template = loader.get_template('welkom/welkomhtml.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def register(request):
    # Only runs when te form is returnd
    if request.method == 'POST':
        name = request.POST['your_name']
        password = request.POST['password']
        email = request.POST['email']
        check_name_exsists = User.objects.filter(username=name)
        if check_name_exsists:
            return render(request, 'welkom/register.html',
                          {'error_message': "This name is already used"})
        else:
            User.objects.create_user(username=name, email=email, password=password)
            return HttpResponseRedirect(reverse('welkom:welkom'))

    return render(request, 'welkom/register.html')


def login(request):

    # Only runs when te form is returnd
    if request.method == 'POST':

        # Checks wheter browser accepts the cookie (it is set below)
        if request.session.test_cookie_worked():

            request.session.delete_test_cookie()

            username = request.POST.get('your_name')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/account/loggedin/")

            else:
                # Show an error page
                return HttpResponseRedirect("/account/invalid/")

        else:
            return HttpResponse("Please enable cookies and try again.")

    # Set the test cookie. is only set when method != POST
    request.session.set_test_cookie()

    return render(request, 'welkom/login.html')



