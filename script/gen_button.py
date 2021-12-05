
from check_link import is_absolute
from domain import get_domain
from check_link import check_link # Todo: not used

def get_button_str(link, text):
	return 	'				<a href="%s" target="_blank" class="btn btn-outline-secondary btn-sm" role="button">' % link + ' %s' % text + '</a>\n'

def get_button_str_inplace(link, text):
	return 	'				<a href="%s" class="btn btn-outline-secondary btn-sm" role="button">' % link + '%s' % text + '</a>\n'

def get_button_str_all(record):
	# this order in this function will determine the order of buttons
	button = ''
	if 'web' in record:
		button += get_button_str(record['web'], 'Project Page')
	if 'web_inplace' in record:
		button += get_button_str_inplace(record['web_inplace'], 'Project Page')
	if 'pdf' in record:
		button += get_button_str(record['pdf'], 'Paper')
	if 'supp' in record:
		button += get_button_str(record['supp'], 'Supplement')
	if 'poster' in record:
		button += get_button_str(record['poster'], 'Poster')
	if 'code' in record:
		button += get_button_str(record['code'], 'Code')
	if 'executable' in record:
		button += get_button_str(record['executable'], 'Executable')
	if 'data' in record:
		button += get_button_str(record['data'], 'Data')
	if 'video' in record:
		button += get_button_str(record['video'], 'Video')
	# if 'bibtex' in record:
	# 	button += get_button_str(record['bibtex'], 'Bibtex')
	if 'tutorial' in record:
		button += get_button_str(record['tutorial'], 'Tutorial')
	return button
