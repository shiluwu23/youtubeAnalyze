from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
import time

from . import youtube_lib


# Create your views here.
def get_token(request):
	crtuser = request.user
	social = crtuser.social_auth.get(provider='google-oauth2')
	auth_time = social.extra_data['auth_time']
	expire_time = social.extra_data['expires']
	if time.time() - auth_time > expire_time:
		raise Exception('Your AOuth2 has expired. Please log in again.')
	token = social.extra_data['access_token']
	return token


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

def my_youtube_stats(request):
	try:
		token = get_token(request)
	except Exception as e:
		result = {'err_msg':str(e)}
		result['err_msg'] += ' Please try log in again.'
		return render(request, 'ytb_myYoutube.html', result)
	result = youtube_lib.mine_channel_list(token)
	tmp = youtube_lib.list_items_num(result['mine_like_id'], token)
	result['mine_like_num'] = tmp
	return render(request, 'ytb_myYoutube.html', result)


def ytb_top_video(request):
	result = youtube_lib.top_videos(10)
	for i in range(len(result['videos'])):
		tmp = result['videos'][i]['snippet']['publishedAt']
		tmp = tmp.replace('T', ' ')
		tmp = tmp.replace('Z', '')
		result['videos'][i]['snippet']['publishedAt'] = tmp[:-4]

		vid = result['videos'][i]['id']['videoId']
		count = youtube_lib.video_viewCount(vid)
		count = int(count)
		count = format(count, ',')
		result['videos'][i]['views'] = count
		result['videos'][i]['rank'] = i+1
		result['videos'][i]['odd'] = (i+1)%2
	return render(request, 'ytb_topvideo.html', result)






# useless functions
def mylogin(request):
    return render(request, 'login.html')

def helloworld(request):
    return HttpResponse('Hello world')