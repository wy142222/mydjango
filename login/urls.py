
from django.urls import path, re_path

from login.views import index, detail, get,post,set_cooking

urlpatterns = [
    # http://127.0.0.1:8000/index/
    path('index/', index,name='home'),
    re_path('(?P<user>\w*)/(?P<password>\d+)/', detail),
    path('get/', get),
    path('post/', post),
    path('set_cookie/', set_cooking),
]