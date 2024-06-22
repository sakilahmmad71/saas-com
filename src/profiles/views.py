from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def profile_list_view(request, *args, **kwargs):
    context = {"profiles": User.objects.filter(is_active=True)}
    return render(request, "pages/profiles.html", context)


@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    # Printout the permissions
    print(user.has_perm("subscriptions.basic"))
    print(user.has_perm("subscriptions.pro"))
    print(user.has_perm("subscriptions.advance"))
    profile_user_obj = get_object_or_404(User, username=username)

    context = {
        "username": profile_user_obj.get_username(),
        "profile": profile_user_obj,
        "basic_subscription": user.has_perm("subscriptions.basic"),
        "pro_subscription": user.has_perm("subscriptions.pro"),
        "advance_subscription": user.has_perm("subscriptions.advance"),
    }
    return render(request, "pages/profile.html", context)
