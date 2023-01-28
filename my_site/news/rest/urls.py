from rest_framework import routers
from news.rest.views import NewsViewSet


router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
