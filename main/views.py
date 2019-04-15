from django.http import HttpResponse


def index(request):
    return HttpResponse("Moin das hier ist das Skelett der Protesthub seite")
# Create your views here.
