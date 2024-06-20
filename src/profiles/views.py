from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    profile_user_obj = get_object_or_404(User, username=username)
    return render(
        request, "pages/profile.html", {"username": profile_user_obj.get_username()}
    )
