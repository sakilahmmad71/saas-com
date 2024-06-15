from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request, *args, **kwargs):
    # print("🚀 ~ login_view ~ request.method", request.method)
    # print("🚀 ~ login_view ~ request.POST", request.POST)

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
