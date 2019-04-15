from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

from .models import Demo
import operator

from django.db.models import Q


def index(request):
    latest_demos = Demo.objects.order_by("-created_at")[:10]
    template = loader.get_template("main/index.html")
    output = {
        "latest_demos": latest_demos,
    }
    return HttpResponse(template.render(output, request))

def single_site(request):
    single_demo=Demo.objects("-is_like")[:1]
    template =loader._get_template("main/demo.html")
    output = {
        "demo": single_demo,
    }
    return HttpResponse(template.render(output, request))

class search_view(TemplateView):
    template_name="main/search.html"

    def get(self,request,*args,**kwargs):
        q=request.GET.get("q","q")
        self.results=Demo.objects.filter(Q(title__icontains=q) | Q(adress__icontains=q) | Q(organizer__icontains=q) | Q(starting_time__icontains=q) | Q(ending_time__icontains=q) | Q(description__icontains=q))

        return super().get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)
# Create your views here.
