import json
from util import authorlist_to_text
from gen_button import get_button_str_all

def write_html(file, data):
	f = open(file, "w")
	# github button
	f.write('<script async defer src="https://buttons.github.io/buttons.js"></script>\n')
	f.write('<div class="container"> <!-- begin of publication list -->\n\n')
	for idx, year in enumerate(data):
		print_year = False
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['type'] == 'international':
						print_year = True
		if print_year:
			if idx != 0:
				f.write('<hr>\n') # adding horizontal line for every years except for the first appearing year
			# adding year
			f.write('<div class="container">\n'+
					'<div class="row">\n'+
					'	<div class="col-lg-12 text-start">\n'+
					'		<h2 class="name">%s</h2>\n' % year +
					'	</div>\n'+
					'</div>\n'+
					'</div>\n\n')
		# list up international
		items_international = []
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['type'] == 'international':
						items_international.append(i)
		if len(items_international) == 0:
			continue
		# adding elements
		f.write('<div class="container">\n'+
				'	<div class="row gx-5 gy-5">\n')
		for i in items_international:
			f.write(
				'		<div class="col-lg-4 text-center">'
				# Thumbnail image
				'			<img src="%s" class="mb-3 img-fluid rounded float-center img-thumbnail">\n' % i['image'] +
				# Paper information
				'			<h4>%s</h4>\n' % i['title'] +
				'			<p>%s. ' % authorlist_to_text(i['author']) +
				'			<em>%s</em><br>\n' % (i['venue'] + ", " + year) +
				'			%s' % (i['comment'] if 'comment' in i else '') +
				'			%s' % (i['github'] if 'github' in i else '') + '</p>\n' +
				# Buttons
				get_button_str_all(i) +
				'		</div>\n')
		f.write(
			'	</div>\n'+
			'</div>\n\n')
	f.write('</div>  <!-- end of publication list -->\n\n')
	f.close()


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	write_html('../source/html/publications.html', data)