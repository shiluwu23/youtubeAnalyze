from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User

from . import youtube_lib


# Create your views here.
def youtubeRoot(request):
    return render(request, 'youtube.html')

def myLogout(request):
	logout(request)
	return render(request, 'youtube.html')

def channel_info_home(request):
	return render(request, 'ytb_searchchannel.html')

def channel_info_search(request):
	result = {}
	if request.POST:
		cid = request.POST.get('cid')
		result = youtube_lib.channel_list(cid)
	return render(request, 'ytb_searchchannel.html', result)

def get_token(request):
	crtuser = request.user
	social = crtuser.social_auth.get(provider='google-oauth2')
	token = social.extra_data['access_token']
	return token

def aboutUs(request):
	return render(request, 'root.html')

# useless functions
def mylogin(request):
    return render(request, 'login.html')

def helloworld(request):
    return HttpResponse('Hello world')

def searchvideo(request):
    ctx = {}
    if request.POST:
        result = youtube_lib.youtube_search(request.POST['q'], max_results=20)
        ctx['result'] = ''
        num = 1
        for i in result[1]:
            ctx['result'] = ctx['result'] + '{0}. '.format(num) + i['snippet']['title'] + '\n'
            num += 1
    return render(request, "youtube.html", ctx)

