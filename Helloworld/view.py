from django.http import HttpResponse
from django.shortcuts import render
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyD4SUyqJ5Nk5OiRl5-tVglDoBF3yYndgxc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

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
 
def root(request):
    return render(request, 'root.html')

def youtube(request):
    return render(request, 'youtube.html')

def searchinyoutube(request):
    ctx = {}
    if request.POST:
        result = youtube_search(request.POST['q'], max_results=10)
        ctx['result'] = ''
        for i in result[1]:
            ctx['result'] = ctx['result'] + i['snippet']['title'] + '\n'
    return render(request, "youtube.html", ctx)