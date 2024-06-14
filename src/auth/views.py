from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request, *args, **kwargs):
    # Getting the username and password from the form
    username = request.POST.get("username")
    password = request.POST.get("password")

    # Create a context dictionary to pass data to the
    context = {"username": username, "password": password}

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    # Check if the user is authenticated
    if user is not None:
        context["user"] = user
        context["valid"] = True

        # Login the user
        login(request, user)

    # return the context data to the login.html template
    return render(request, "auth/login.html", context)
