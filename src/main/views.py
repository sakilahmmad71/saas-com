from django.shortcuts import render

from visits.models import Visit


def home_view(request, *args, **kwargs):
    # Queryset
    qa = Visit.objects.all()
    page_qs = Visit.objects.filter(path=request.path)

    # Context data
    context = {
        "name": "Shakil Ahmed",
        "age": 25,
        "job": "Software Engineer",
        "title": "Home Page",
        "content": "Welcome to the home page!",
        "author": "Shakil Ahmed",
        "keywords": "django, python, web development",
        "description": "This is a Django web application built for learning purposes.",
        "url": "https://www.shakilahmed.me",
        "page_visit_count": page_qs.count(),
        "total_visit_count": qa.count(),
    }

    # HTML template
    html_template = "pages/home.html"
    # Create a new Visit object
    Visit.objects.create(path=request.path)
    # Render the HTML template with the context data
    return render(request, html_template, context)


def about_view(request, *args, **kwargs):
    # Queryset
    qa = Visit.objects.all()
    page_qs = Visit.objects.filter(path=request.path)

    # Context data
    context = {
        "name": "Shakil Ahmed",
        "age": 25,
        "job": "Software Engineer",
        "title": "About Page",
        "content": "Welcome to the about page!",
        "author": "Shakil Ahmed",
        "keywords": "django, python, web development",
        "description": "This is a Django web application built for learning purposes.",
        "url": "https://www.shakilahmed.me",
        "page_visit_count": page_qs.count(),
        "total_visit_count": qa.count(),
    }

    # HTML template
    html_template = "pages/home.html"
    # Create a new Visit object
    Visit.objects.create(path=request.path)
    # Render the HTML template with the context data
    return render(request, html_template, context)


VALID_CODE = "123456"


def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get("protected_page_allowed", False) or False

    if request.method == "POST":
        code = request.POST.get("code") or None
        if code == VALID_CODE:
            request.session["protected_page_allowed"] = True

    if is_allowed:
        return render(request, "protected/entry.html", {})

    return render(request, "protected/view.html", {})
