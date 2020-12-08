from django.urls import path, re_path
from .views import GetSerialList, GetVideoList

app_name = 'exportVideo'
urlpatterns = [
    path('getSerialList/', GetSerialList.as_view(), name='getSerialList'),
    path('getVideoList/', GetVideoList.as_view(), name='getVideoList'),
]