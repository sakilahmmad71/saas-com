from django.shortcuts import render

from visits.models import Visit


def home_page_view(request, *args, **kwargs):
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