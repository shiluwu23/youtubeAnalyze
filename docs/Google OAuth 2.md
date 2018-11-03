# How to login with Google account on your own website

Simply running localhost can't use Google OAuth2.

If you want use that function, you should customize it.
1. Go to [Google Cloud Platform - APIs and Services - Credentials](https://console.cloud.google.com/apis/credentials)

2. Click ```Create credentials``` - ```OAuth client ID``` - ```Web Application```

3. Fill the ```Authorized redirect URIs``` using your domain name ( I don't know whether using your localhost IP adress is possible, I've never tried that. Howerver, Google says it 'Cannot be a public IP address'. So maybe Login with Google is imposiible in localhost ), like
```
http://www.zhduan.com/youtube/oathcomplete/google-oauth2/
and
http://zhduan.com/youtube/oathcomplete/google-oauth2/
```

4. Finishing creating credentials, then you will get your ```Client ID``` and ```Client secret```

5. At [Google Cloud Platform - APIs and Services - OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent), fill the information about your website

6. Replace the ```SOCIAL_AUTH_GOOGLE_OAUTH2_KEY``` and ```SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET``` in ```line 145 and 146``` in ```/zhduan/zhduan/settings.py``` with your ```Client ID``` and ```Client secret```, instead of mine.

7. Then you are done, try to login with Google account on your website
