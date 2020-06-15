from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(" DbG-1 : " + str(args))
    print(" DbG-2 : " + str(kwargs))
    print(" DbG-3 : " + str(request.user))
    print(" DbG-4 : " + str(request))
    # return HttpResponse("<H6>This is View</H6>")
    return render(request, "home.html", {})