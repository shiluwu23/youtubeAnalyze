from urllib import request
import json

class ytbAPI(object):

	DATA_V3_BASE = 'https://www.googleapis.com/youtube/v3/'
	__API_KEY = ""

	def __init__(self):
		self.keyStr = '&key=' + self.__API_KEY
		self.url = self.DATA_V3_BASE

	def scope(self, scp):
		'''
		scp: str, name of scope
		'''
		self.scopeStr = scp + '?'
		self.url += self.scopeStr

	def part(self, *args):
		'''
		*args: tuple of str, input 'part'
		'''
		if len(args)==0:
			raise Exception('No input part parameter')
		self.partStr = 'part='
		for arg in args:
			self.partStr += arg + '%2C'
		self.partStr = self.partStr[:-3]
		self.url += self.partStr

	def id(self, i):
		'''
		i: str, input id
		'''
		self.idStr = '&id=' + i
		self.url += self.idStr
	
	def mine(self, m=True):
		'''
        m: bool, the value of 'mine'
        '''
		if m:
			self.mineStr = '&mine=true'
			self.url += self.mineStr

	def maxResults(self, m):
		'''
		m: str or int or float, the max number of results per page
		'''
		m = int(m)
		m = str(m)
		self.maxStr = '&maxResults=' + m
		self.url += self.maxStr

	def playlistId(self, i):
		'''
		i: str, input playlist id
		'''
		self.listIdStr = '&playlistId=' + i
		self.url += self.listIdStr

	def order(self, o):
		'''
		o: str, the type of order
		'''
		self.orderStr = '&order=' + o
		self.url += self.orderStr
	
	def safeSearch(self, s='none'):
		'''
		s: str, 'moderate', 'none', 'strict'
		'''
		self.safeSrchStr = '&safeSearch=' + s
		self.url += self.safeSrchStr

	def type(self, t):
		'''
		t: str, 'channel', 'playlist', 'video'
		'''
		self.typeStr = '&type=' + t
		self.url += self.typeStr

	def videoCategoryId(self, i):
		'''
		i: str, video category id
		'''
		self.vctgyIdStr = '&videoCategoryId=' + i
		self.url += self.vctgyIdStr

	def publishedAfter(self, t):
		'''
		t: str, the time, like '2018-01-01T00:00:00Z'
		'''
		t = t.replace(':','%3A')
		self.pbAfterStr = '&publishedAfter=' + t
		self.url += self.pbAfterStr

	def videoDuration(self, d='any'):
		'''
		d: str, the duration of video, can be:
								'any',
								'long' > 20 mins,
								'medium' 4 - 20 mins,
								'short' < 4 mins
		'''
		valid = ('any','long','medium','short')
		assert d in valid, '{} is not a valid duration'.format(d)
		self.vDrtnStr = '&videoDuration=' + d
		self.url += self.vDrtnStr

	#---------------------------------------------------

	def key(self, k=False):
		'''
		k: str, the api_key of Google Cloud
		'''
		if k:
			self.keyStr = '&key=' + k
		self.url += self.keyStr
	
	def access_token(self, t):
		'''
		t: str, input OAuth 2 access token
		'''
		self.tokenStr = '&access_token=' + t
		self.url += self.tokenStr

	def GET(self):
		'''
		return: dictionary, response of youtube/google
		'''
		try:
			req = request.Request(self.url)
			page = request.urlopen(req).read()
			page = page.decode('utf-8')
			return json.loads(page)
		except Exception as e:
			return {'error': e}
