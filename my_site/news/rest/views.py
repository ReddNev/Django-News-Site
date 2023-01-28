from rest_framework import viewsets
from news.rest.serializers import NewsSerializer

from news.models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def upload_docs(request):
        pass

