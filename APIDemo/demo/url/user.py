from django.conf.urls import url
from demo.forms.user import UserRegister

app_name = 'demo'

urlpatterns = [
    url(r'^register/$', UserRegister.as_view(), name='register'),
]
