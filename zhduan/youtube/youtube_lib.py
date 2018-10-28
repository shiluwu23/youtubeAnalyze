from googleapiclient.discovery import build
from urllib import request
import json
# from googleapiclient.errors import HttpError
# from oauth2client.tools import argparser

DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def channel_list(cid):
	scope = 'https://www.googleapis.com/youtube/v3/channels'
	parameter = '?part=topicDetails%2Csnippet%2CcontentDetails%2Cstatistics'
	channel = '&id=' + cid
	key = '&key=' + DEVELOPER_KEY
	GET_str = scope + parameter + channel + key
	print(GET_str)

	req = request.Request(GET_str)
	page = request.urlopen(req).read()
	page = page.decode('utf-8')
	response = json.loads(page)

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



# useless functions
'''
def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
		developerKey=DEVELOPER_KEY)

	search_response = youtube.search().list(
		q=q,
		type="video",
		pageToken=token,
		order = order,
		part="id,snippet",
		maxResults=max_results,
		location=location,
		locationRadius=location_radius

	).execute()

	videos = []

	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			videos.append(search_result)
	try:
		nexttok = search_response["nextPageToken"]
		return(nexttok, videos)
	except Exception as e:
		nexttok = "last_page"
		return(nexttok, videos)

def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response
'''