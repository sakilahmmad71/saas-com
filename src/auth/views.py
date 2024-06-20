from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings

from django.contrib.auth import get_user_model

LOGIN_URL = settings.LOGIN_URL
User = get_user_model()


# Create your views here.
def login_view(request, *args, **kwargs):
    if request.method == "POST":
        # Getting the username and password from the form
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None

        if all([username, password]):
            # Create a context dictionary to pass data to the
            context = {"username": username, "password": password}
            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # Check if the user is authenticated
            if user is not None:
                print("User is authenticated")
                # Login the user
                login(request, user)
                redirect("/")

    # return the context data to the login.html template
    return render(request, "pages/login.html", {})


def register_view(request, *args, **kwargs):
    if request.method == "POST":
        # Getting the username and password from the form
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None

        if all([username, email, password]):
            # Create a context dictionary to pass data to the
            context = {"username": username, "email": email, "password": password}
            print("context", context)

            try:
                # Create a new user
                user = User.objects.create_user(username, email, password)
                user.save()
                print("User created")
            except Exception as e:
                print("Error creating user", e)
                pass

    # return the context data to the login.html template
    return render(request, "pages/register.html", {})


@login_required
def user_only_view(request, *args, **kwargs):
    return render(request, "pages/user_only.html", {})


@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, "pages/staff_only.html", {})
