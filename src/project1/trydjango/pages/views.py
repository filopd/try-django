from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<H6>This is View</H6>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_contact = {
        "f_name": "Priyesh",
        "l_name": "Naik",
        "my_age": 26,
        "skills": ['python','java','bash']
    }
    return render(request, "contact.html", my_contact)