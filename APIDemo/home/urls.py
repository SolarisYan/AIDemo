from django.conf.urls import url
from home.views import index

urlpatterns = [
    url(r'^$', index.Index.as_view(), name='index'),
]
