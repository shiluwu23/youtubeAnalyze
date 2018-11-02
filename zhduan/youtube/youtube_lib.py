from .ytbAPI import ytbAPI
import time

def pre_time_RFC3339(d=0, w=0, m=0, y=0):
	'''
	minus current local time with the parameter,
	then return the time in format of RFC 3339
	d: int, day
	w: int, week
	m: int, month
	y: int, year
	return: str, like '2018-10-30T14:03:06Z'
	'''
	assert d >= 0
	assert w >= 0
	assert m >= 0
	assert y >= 0

	lt = time.time()
	if d:
		lt -= 86400*d
	if w:
		lt -= 604800*w
	if m:
		lt -= 2592000*m
	if y:
		lt -= 31536000*y
	lt = time.localtime(lt)
	timeStr = time.strftime("%Y-%m-%dT%H:%M:%SZ", lt)

	return timeStr


def channel_list(cid):
	'''
	cid: channel id
	return: key-value dict
	'''
	ytb0 = ytbAPI()
	ytb0.scope('channels')
	ytb0.part('topicDetails','snippet', 'contentDetails','statistics')
	ytb0.id(cid)
	ytb0.key()
	response = ytb0.GET()

	re_map = {}
	if 'error' in response:
		re_map['err_msg'] = 'Error from google: Invalid channel id'
		return re_map
	if not 'items' in response:
		re_map['err_msg'] = 'No item in response: Invalid channel id'
		return re_map
	elif len(response['items'])==0:
		re_map['err_msg'] = 'No result: Invalid channel id'
		return re_map
	
	items0 = response['items'][0]
	re_map['ch_title'] = items0['snippet']['title']
	re_map['ch_id'] = items0['id']
	re_map['ch_viewCount'] = items0['statistics']['viewCount']
	re_map['ch_videoCount'] = items0['statistics']['videoCount']
	if items0['statistics']['hiddenSubscriberCount'] == True:
		re_map['chl_subCount'] = 'invisible'
	else:
		re_map['chl_subCount'] = items0['statistics']['subscriberCount']

	return re_map


def mine_channel_list(token):
	'''
	token: access token of OAuth 2 user
	return: key-value dict
	'''
	ytb0 = ytbAPI()
	ytb0.scope('channels')
	ytb0.part('snippet', 'contentDetails', 'statistics')
	ytb0.mine()
	ytb0.access_token(token)
	response = ytb0.GET()

	re_map = {}
	if 'error' in response:
		re_map['err_msg'] = response['error']['message']
		return re_map
	elif not 'items' in response:
		re_map['err_msg'] = 'No item in response.'
		return re_map
	
	items0 = response['items'][0]
	try:
		re_map['mine_title'] = items0['snippet']['title']
		re_map['mine_ch_id'] = items0['id']
		tmp = items0['snippet']['publishedAt']
		tmp = tmp.replace('T', ' ')
		tmp = tmp.replace('Z','')
		re_map['publishDate'] = tmp[:-4]
		re_map['thumb_88_url'] = items0['snippet']['thumbnails']['default']['url']
		re_map['mine_like_id'] = items0['contentDetails']['relatedPlaylists']['likes']
		re_map['mine_upload'] = items0['contentDetails']['relatedPlaylists']['uploads']
		re_map['mine_sub_num'] = my_sub_num(token)
	except Exception as e:
		re_map['err_msg'] = e
		return re_map
	
	return re_map


def my_sub_num(token):
	'''
	calculate and return the number of my subscriptions
	token: str, OAuth 2 user's access token
	return: str, user's subscription number
			or str, the exception message
	'''
	ytb0 = ytbAPI()
	ytb0.scope('subscriptions')
	ytb0.part('contentDetails')
	ytb0.mine()
	ytb0.access_token(token)
	response = ytb0.GET()

	try:
		num = response['pageInfo']['totalResults']
	except Exception as e:
		return e
	return num


def list_items_num(lid, token):
	'''
	lid: playlist id
	token: access token of OAuth 2 user
	return: int, number of items of the list
	'''
	ytb0 = ytbAPI()
	ytb0.scope('playlistItems')
	ytb0.part('snippet', 'contentDetails')
	ytb0.maxResults(1)
	ytb0.playlistId(lid)
	ytb0.access_token(token)
	response = ytb0.GET()

	if 'error' in response:
		return response['error']['message']
	elif not 'pageInfo' in response:
		return 'no page info in response'
	else:
		return response['pageInfo']['totalResults']
	

def top_videos(num=10, after=None, cid='all', du='any'):
	'''
	num: int, how many videos to return
	after: str,  the time, like '2018-01-01T00:00:00Z'
	cid: str, video category id
	du: str, the duration of video: 'any',
									'long' > 20 mins,
									'medium' 4 - 20 mins,
									'short' < 4 mins

	return: dict, ['videos']: a list of (num) dicts, ['err_msg']
	'''
	ytb0 = ytbAPI()
	ytb0.scope('search')
	ytb0.part('snippet')
	ytb0.maxResults(num)
	ytb0.order('viewCount')
	ytb0.safeSearch('none')
	ytb0.type('video')
	ytb0.key()
	if after:
		ytb0.publishedAfter(after)
	if cid != 'all':
		ytb0.videoCategoryId(cid)
	if du != 'any':
		ytb0.videoDuration(du)

	print(ytb0.url)
	response = ytb0.GET()

	re_map = {}
	if 'error' in response:
		re_map['err_msg'] = response['error']['message']
		return re_map
	elif not 'items' in response:
		re_map['err_msg'] = 'No item in response.'
		return re_map
	
	re_map['videos'] = response['items'] # a list
	return re_map


def video_list(vid, *args):
	'''
	vid: str, video id
	*args: parts of request
	return: dict, json file
	'''
	ytb0 = ytbAPI()
	ytb0.scope('videos')
	ytb0.part(*args)
	ytb0.id(vid)
	ytb0.key()
	response = ytb0.GET()

	if 'error' in response:
		raise Exception(response['error']['message'])
	elif not 'items' in response:
		raise Exception('No items in response')

	return response['items'][0]


def video_viewCount(vid):
	'''
	Get the view count of a video
	vid: str, video id
	return: str, the number of views, like '320000'
	'''
	stat = video_list(vid, 'statistics')
	return stat['statistics']['viewCount']


# def most_video_ch():

