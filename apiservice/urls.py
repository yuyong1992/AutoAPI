from apiservice import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'collection', views.CollectionView)
router.register(r'api', views.ApiView)
router.register(r'case', views.CaseView)
router.register(r'result', views.ResultView)

urlpatterns = [
    url(r'^', include(router.urls))
]
