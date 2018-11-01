from .ytbAPI import ytbAPI

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
		re_map['publishDate'] = tmp
		re_map['thumb_88_url'] = items0['snippet']['thumbnails']['default']['url']
		re_map['mine_like_id'] = items0['contentDetails']['relatedPlaylists']['likes']
		re_map['mine_upload'] = items0['contentDetails']['relatedPlaylists']['uploads']
	except Exception as e:
		re_map['err_msg'] = e
		return re_map
	
	return re_map


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
	

def top_videos(num):
	'''
	num: int, how many videos to return
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

