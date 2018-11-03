# youtubeAnalyzeProject
BU EC601 Project

# Our Web App
www.zhduan.com/youtube

It is still in progress.

# Our codes
Our whole project codes are in folder ```zhduan```. There are two ways you can reuse our codes.

1. Run our website on your own computer.
2. Use our YouTube API library.

# Run our website
We use [Django](https://www.djangoproject.com) as our server framework. You can try our website on your localhost simply by the following steps.

0. Make sure you have a python 3.x

1. Install [Django](https://www.djangoproject.com) and [Python Social Auth of Django](https://github.com/python-social-auth/social-app-django)
```bash
pip install Django
pip install social-auth-app-django
```
2. Download our codes, open terminal in ```/zhduan```, then
```bash
python manage.py runserver 0:80
or
python manage.py runserver
```
3. You are done! Open your browser and enter ```localhost```(python manage.py runserver 0:80) or ```localhost:8000```(python manage.py runserver), then you should see a UI of the website.

4. Open ```/zhduan/youtube/ytbAPI.py```, enter your Google API Key at ```line 7```. For how to get a Google API Key, you can [Google it](https://www.google.com/search?source=hp&ei=XtrdW_ujLq2k_Qb5w6m4AQ&q=google+api+key&btnK=Google+Search&oq=google+api+key&gs_l=psy-ab.3..0l10.1453.4574..4861...0.0..0.176.1171.14j1......0....1..gws-wiz.....0..0i131j0i10.ugf-rXJhE4k).

5. Now you can access most functions of the website on your localhost, except ones need OAuth 2.

# Use our YouTube API library
If you just want to try our YouTube API instead of the whole project, take the following steps. (Make sure you have Python 3.x)

0. ```/zhduan/youtube/ytbAPI.py``` is a simple API to connect YouTube/Google. ```/zhduan/youtube/youtube_lib.py``` contains many functions which use ```ytbAPI.py``` to connect YouTube/Google. There are build-in comments in these files, and they are pretty ez to read.

1. Install urllib3
```bash
pip install urllib3
```

2. Download ```/zhduan/youtube/ytbAPI.py```. Put it in the same folder with your own codes. Enter your Google API Key at ```line 7```. For how to get a Google API Key, you can [Google it](https://www.google.com/search?source=hp&ei=XtrdW_ujLq2k_Qb5w6m4AQ&q=google+api+key&btnK=Google+Search&oq=google+api+key&gs_l=psy-ab.3..0l10.1453.4574..4861...0.0..0.176.1171.14j1......0....1..gws-wiz.....0..0i131j0i10.ugf-rXJhE4k).

3. You are done!

3. Here is an example of getting top 10 viewed video in YouTube in the history. There are more in ```youtube_lib.py```.
```python
ytb0 = ytbAPI()
ytb0.scope('search')
ytb0.part('snippet')
ytb0.maxResults(10)
ytb0.order('viewCount')
ytb0.type('video')
ytb0.key()
response = ytb0.GET()

for i in response['items']:
    print(i['snippet']['title'])
```
