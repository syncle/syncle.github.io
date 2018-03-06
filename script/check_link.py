
import os, sys
if (sys.version_info > (3, 0)):
	pversion = 3
else:
	pversion = 2

if pversion == 3:
	import urllib.request
	from urllib.parse import urlparse
elif pversion == 2:
	import urllib2
	from urlparse import urlparse

def is_absolute(url):
	return bool(urlparse(url).netloc)

def check_url(link):
	# only retrieve HEAD to save time.
	if is_absolute(link):
		if pversion == 3:
			try:
				request = urllib.request.Request(link)
				request.get_method = lambda: 'HEAD'
				urllib.request.urlopen(request)
			except urllib.request.HTTPError:
				print('Warning:: broken link %s' % link)
		elif pversion == 2:
			try:
				request = urllib2.Request(link)
				request.get_method = lambda: 'HEAD'
				urllib2.urlopen(request)
			except urllib2.HTTPError:
				print('Warning:: broken link %s' % link)
	else:
		root_folder = os.path.dirname(os.getcwd())
		abs_path = os.path.join(root_folder, link)
		if os.path.exists(abs_path) == False:
			print('Warning:: broken link %s' % abs_path)
