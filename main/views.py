from django.http import HttpResponse
from django.template import loader

from .models import Demo


def index(request):
    latest_demos = Demo.objects.order_by("-created_at")[:10]
    template = loader.get_template("main/index.html")
    output = {
        "latest_demos": latest_demos,
    }
    return HttpResponse(template.render(output, request))
# Create your views here.
