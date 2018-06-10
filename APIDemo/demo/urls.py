from django.conf.urls import url, include
from demo.views import index

app_name = 'demo'

urlpatterns = [
    url(r'^$', index.Index.as_view(), name='index'),
    url(r'^user/', include('demo.url.user', namespace='user')),
]
