from django.conf.urls import url  # , include
from demo.views import index

urlpatterns = [
    url(r'^$', index.Index.as_view(), name='index'),
]
