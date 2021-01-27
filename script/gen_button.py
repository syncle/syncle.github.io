
import record

from check_link import is_absolute
from domain import get_domain
from check_link import check_link

def get_button_str_inplace(link, glyphicon, text):
	return 	'		<a href="%s" class="btn btn-default" role="button">\n' % link + \
			'			<span class="glyphicon glyphicon-%s"></span>' % glyphicon + ' %s\n' % text + \
			'		</a>\n'

def get_button_str(link, glyphicon, text):
	return 	'		<a href="%s" target="_blank" class="btn btn-default" role="button">\n' % link + \
			'			<span class="glyphicon glyphicon-%s"></span>' % glyphicon + ' %s\n' % text + \
			'		</a>\n'

def get_button_str_predefined(link, type, CHECK_LINK = False):
	if CHECK_LINK:
		check_link(link)
	if not is_absolute(link):
		link = get_domain() + '/' + link
	if type == 'Paper':
		return get_button_str(link, 'file', 'Paper')
	elif type == 'Code':
		return get_button_str(link, 'pencil', 'Code')
	elif type == 'Data':
		return get_button_str(link, 'download-alt', 'Data')
	elif type == 'Project Page':
		return get_button_str(link, 'home', 'Project Page')
	elif type == 'Project Page Inplace':
		return get_button_str_inplace(link, 'home', 'Project Page')
	elif type == 'Video':
		return get_button_str(link, 'play', 'Video')
	elif type == 'Supplementary':
		return get_button_str(link, 'paperclip', 'Supplementary')
	elif type == 'Bibtex':
		return get_button_str(link, 'list', 'Bibtex')
	elif type == 'Executable':
		return get_button_str(link, 'floppy-disk', 'Executable')
	elif type == 'Poster':
		return get_button_str(link, 'blackboard', 'Poster')
	elif type == 'Tutorial':
		return get_button_str(link, 'book', 'Tutorial')
	else:
		return ''

def get_button_str_all(record):

	button_pdf = ''
	button_code = ''
	button_data = ''
	button_web = ''
	button_web_inplace = ''
	button_video = ''
	button_supp = ''
	button_bibtex = ''
	button_executable = ''
	button_poster = ''
	button_tutorial = ''

	if 'pdf' in record:
		button_pdf = get_button_str_predefined(record['pdf'], 'Paper')
	if 'code' in record:
		button_code = get_button_str_predefined(record['code'], 'Code')
	if 'data' in record:
		button_data = get_button_str_predefined(record['data'], 'Data')
	if 'web' in record:
		button_web = get_button_str_predefined(record['web'], 'Project Page')
	if 'web_inplace' in record:
		button_web_inplace = get_button_str_predefined(record['web_inplace'], 'Project Page Inplace')
	if 'video' in record:
		button_video = get_button_str_predefined(record['video'], 'Video')
	if 'supp' in record:
		button_supp = get_button_str_predefined(record['supp'], 'Supplementary')
	if 'bibtex' in record:
		button_bibtex = get_button_str_predefined(record['bibtex'], 'Bibtex')
	if 'executable' in record:
		button_executable = get_button_str_predefined(record['executable'], 'Executable')
	if 'poster' in record:
		button_poster = get_button_str_predefined(record['poster'], 'Poster')
	if 'tutorial' in record:
		button_tutorial = get_button_str_predefined(record['tutorial'], 'Tutorial')

	# this combined html script will determine the order of buttons
	button = button_web + button_web_inplace + \
			button_pdf + button_supp + button_poster + \
			button_video + button_bibtex + \
			button_code + button_executable + button_data + button_tutorial
	return button
