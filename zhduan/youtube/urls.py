from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.youtubeRoot, name = 'youtubehome'),
    path('search_video', views.searchvideo),
    # path('login', views.login, name='ytblogin'),
    path('logout', views.myLogout, name='ytblogout'),
    # path('showtoken', views.show_token, name='showTokenPage'),
    path('channelinfo', views.channel_info_home, name='ChInfoPage'),
    path('channelinfo/search', views.channel_info_search, name='chInfoSearch'),
    path('oath', include('social_django.urls', namespace='social')),
]