
from check_link import is_absolute
from domain import get_domain
from check_link import check_link

def get_button_str_inplace(link, text):
	return 	'			<a href="%s" class="btn btn-outline-secondary btn-sm" role="button">' % link + '%s' % text + '</a>\n'

def get_button_str(link, text):
	return 	'			<a href="%s" target="_blank" class="btn btn-outline-secondary btn-sm" role="button">' % link + ' %s' % text + '</a>\n'

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
		button_pdf = get_button_str(record['pdf'], 'Paper')
	if 'code' in record:
		button_code = get_button_str(record['code'], 'Code')
	if 'data' in record:
		button_data = get_button_str(record['data'], 'Data')
	if 'web' in record:
		button_web = get_button_str(record['web'], 'Project Page')
	if 'web_inplace' in record:
		button_web_inplace = get_button_str_inplace(record['web_inplace'], 'Project Page')
	if 'video' in record:
		button_video = get_button_str(record['video'], 'Video')
	if 'supp' in record:
		button_supp = get_button_str(record['supp'], 'Supplement')
	if 'bibtex' in record:
		button_bibtex = get_button_str(record['bibtex'], 'Bibtex')
	if 'executable' in record:
		button_executable = get_button_str(record['executable'], 'Executable')
	if 'poster' in record:
		button_poster = get_button_str(record['poster'], 'Poster')
	if 'tutorial' in record:
		button_tutorial = get_button_str(record['tutorial'], 'Tutorial')

	# this combined html script will determine the order of buttons
	button = button_web + button_web_inplace + \
			button_pdf + button_supp + button_poster + \
			button_video + button_bibtex + \
			button_code + button_executable + button_data + button_tutorial
	return button
