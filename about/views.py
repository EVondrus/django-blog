from django.shortcuts import render, get_object_or_404
from about.models import About

# Create your views here.
def aboutView(request):
    about = About.objects.order_by("-updated_on").first()
    return render(
        request,
        "about/about.html",
        {"about": about}
    )
