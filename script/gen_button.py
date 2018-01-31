
import record

def get_button_str_inplace(link, glyphicon, text):
	return 	'		<a href="%s" class="btn btn-default" role="button">\n' % link + \
			'			<span class="glyphicon glyphicon-%s"></span>' % glyphicon + ' %s\n' % text + \
			'		</a>\n'

def get_button_str(link, glyphicon, text):
	return 	'		<a href="%s" target="_blank" class="btn btn-default" role="button">\n' % link + \
			'			<span class="glyphicon glyphicon-%s"></span>' % glyphicon + ' %s\n' % text + \
			'		</a>\n'

def get_button_str_predefined(link, type):
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

	if record.pdf != '':
		button_pdf = get_button_str_predefined(record.pdf, 'Paper')
	if record.code != '':
		button_code = get_button_str_predefined(record.code, 'Code')
	if record.data != '':
		button_data = get_button_str_predefined(record.data, 'Data')
	if record.web != '':
		button_web = get_button_str_predefined(record.web, 'Project Page')
	if record.web_inplace != '':
		button_web_inplace = get_button_str_predefined(record.web_inplace, 'Project Page Inplace')
	if record.video != '':
		button_video = get_button_str_predefined(record.video, 'Video')
	if record.supp != '':
		button_supp = get_button_str_predefined(record.supp, 'Supplementary')
	if record.bibtex != '':
		button_bibtex = get_button_str_predefined(record.bibtex, 'Bibtex')
	if record.executable != '':
		button_executable = get_button_str_predefined(record.executable, 'Executable')
	if record.poster != '':
		button_poster = get_button_str_predefined(record.poster, 'Poster')
	if record.tutorial != '':
		button_tutorial = get_button_str_predefined(record.tutorial, 'Tutorial')

	# this combined html script will determine the order of buttons
	button = button_web + button_web_inplace + \
			button_pdf + button_supp + button_poster + \
			button_video + button_bibtex + \
			button_code + button_executable + button_data + button_tutorial
	return button
