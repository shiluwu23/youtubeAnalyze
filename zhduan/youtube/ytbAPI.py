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
	
	def safeSearch(self, s):
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
		req = request.Request(self.url)
		page = request.urlopen(req).read()
		page = page.decode('utf-8')
		return json.loads(page)