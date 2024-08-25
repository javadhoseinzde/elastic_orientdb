from django.urls import path
from apps.elastic.api.api import ElasticApi


urlpatterns = [
    path("elastic", ElasticApi.as_view())
]