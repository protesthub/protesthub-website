from rest_framework import viewsets

from main.api.serializers import searchSerializer
from main.models import Demo


class specificsearchViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = searchSerializer

    def get_queryset(self):

        queryset = Demo.objects.all().order_by('-created_at')
        title = self.request.query_params.get('title', None)
        adress = self.request.query_params.get('adress', None)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if adress is not None:
            queryset = queryset.filter(title__icontains=adress)

        return queryset

# Create your views here.
