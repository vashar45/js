from django.http import HttpResponse


def home(request):
    return HttpResponse("This is a test? Viewers! We are testing how traffic is split")
