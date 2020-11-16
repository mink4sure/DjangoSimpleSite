from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import django.contrib.auth as auth

from django.contrib.auth.models import User

# The view corresponding to the welkompage of the site
def welkom(request):
    # Setting the template for the welkom page
    template = loader.get_template('welkom/welkomhtml.html')
    context = {

    }

    # Rendering the template of the welkom page
    return HttpResponse(template.render(context, request))


# A funtion to register new users
def register(request):
    # Only runs when te form is returnd
    if request.method == 'POST':
        # Getting the entered name, password and email
        name = request.POST['your_name']
        password = request.POST['password']
        email = request.POST['email']

        # Checks wheter this username is already used
        check_name_exsists = User.objects.filter(username=name)
        if check_name_exsists:
            # Sending error message for when name is used
            return render(request, 'welkom/register.html',
                          {'error_message': "This name is already used"})
        else:
            # Creates new user and redirects to the welkom page
            User.objects.create_user(username=name, email=email, password=password)
            return HttpResponseRedirect(reverse('welkom:welkom'))

    # rendering the register page
    return render(request, 'welkom/register.html')


def login(request):

    # Only runs when te form is returnd
    if request.method == 'POST':

        # Checks wheter browser accepts the cookie (it is set below)
        if request.session.test_cookie_worked():

            # Deleting the test cookie to clean up
            request.session.delete_test_cookie()

            # Getting the username and password from the POST method
            username = request.POST.get('your_name')
            password = request.POST.get('password')

            # Checks whether the name and password make a valid combination
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                # Login in user
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/home/")

            else:
                # Show an error page when invalid combo
                return HttpResponseRedirect("/account/invalid/")

        # If de browser does not accept cookies
        else:
            return HttpResponse("Please enable cookies and try again.")

    # Set the test cookie. is only set when method != POST
    request.session.set_test_cookie()

    return render(request, 'welkom/login.html')



