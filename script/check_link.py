
# this script only for Python 3
import urllib.request
from urllib.parse import urlparse
import os

ROOT_FOLDER = os.path.dirname(os.getcwd())

def is_absolute(url):
	return bool(urlparse(url).netloc)

def check_url(link):
	"""
	Checks that a given URL is reachable.
	:param url: A URL
	:rtype: bool
	"""
	if is_absolute(link):
		try:
			request = urllib.request.Request(link)
			request.get_method = lambda: 'HEAD'
			urllib.request.urlopen(request)
		except urllib.request.HTTPError:
			print('Warning:: broken link %s' % link)
	else:
		abs_path = os.path.join(ROOT_FOLDER, link)
		if os.path.exists(abs_path) == False:
			print('Warning:: broken link %s' % abs_path)
