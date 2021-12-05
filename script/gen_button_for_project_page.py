
from gen_button import get_button_str_all
from util import authorlist_to_html_text

def append_button_html(path, data):
	f = open(path, "a")
	f.write(# Buttons
			'<div class="container">\n'+
			'	<div class="row">\n'+
			'		<div class="col-12">\n'+
			'			<h2>Publication(s)</h2>\n')
	for idx, year in enumerate(data):			
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['language'] == 'international':
						f.write(
							# Paper information
							'			<h4>%s</h4>\n' % i['title'] +
							'			<p>%s<br>\n' % authorlist_to_html_text(i['author']) +
							'			%s<br>\n' % i['venue'] +
							'			%s</p>\n' % (i['comment'] if 'comment' in i else '') +
							# Buttons
							get_button_str_all(i) + 
							'<br><br>\n')
	f.write('		</div>\n')
	f.write('	</div>\n')
	f.write('</div>\n')
	f.close()
