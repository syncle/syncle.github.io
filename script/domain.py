
DOMAIN = 'https://jaesik.info'

def get_domain():
	return DOMAIN

def get_full_html_path(path):
	if path.find('http') == -1:
		path = get_domain() + '/' + path
	return path