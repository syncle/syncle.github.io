import json
from gen_button import get_button_str_all

def authorlist_to_text(author):
	# adding special action for my name?
	if len(author) == 2:
		return author[0] + ' and ' + author[1]
	else:		
		s = ''
		for a in author[:-1]:
			s += (a + ', ')
		s += author[-1]
		return s

def write_html(file, data):
	f = open(file, "w")
	# github button
	f.write('<script async defer src="https://buttons.github.io/buttons.js"></script>\n')
	f.write('<div class="container"> <!-- begin of publication list -->\n\n')
	for idx, year in enumerate(data):
		if idx != 0:
			f.write('<hr>\n') # adding horizontal line for every years except for the first appearing year
		# adding year
		f.write('<div class="container">\n'+
				'<div class="row">\n'+
				'	<div class="col-lg-12 text-left">\n'+
				'		<h2 class="name">%s</h2>\n' % year +
				'	</div>\n'+
				'</div>\n'+
				'</div>\n\n')
		# adding elements
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['type'] == 'international':
						f.write('<div class="container">\n'+
							'<div class="row">\n'+
							# Thumbnail image
							'	<div class="col-lg-4 col-lg-offset-1">\n'+
							'		<img src="%s" style="max-height:170px" class="img-responsive center-block img-thumbnail">\n' % i['image'] +
							'	</div>\n'+
							# Paper information
							'	<div class="col-lg-7">\n'+
							'		<h3>%s</h3>\n' % i['title'] +
							'		<p>%s<br>\n' % authorlist_to_text(i['author']) +
							'		%s<br>\n' % i['venue'] +
							'		%s</p>\n' % (i['comment'] if 'comment' in i else '') +
							# Buttons
							get_button_str_all(i) +
							'	</div>\n'+
							'</div>\n'+
							# just for adding some space - not sure style="height" is compatible for browsers
							'<div class="row" style="height: 30px">\n'+
							'</div>\n'+
							'</div>\n\n')
	f.write('</div>  <!-- end of publication list -->\n\n')
	f.close()


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	write_html('../source/publications.html', data)
