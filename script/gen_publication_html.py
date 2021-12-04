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
					'	<div class="col-lg-12 test-start">\n'+
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
		# adding elements
		column_cnt = 0
		for id, i in enumerate(items_international):
			if column_cnt == 0:
				f.write('<div class="container">\n'+
					'	<div class="row">\n')
			f.write(
				'		<div class="col-lg-4 text-left">'
				# Thumbnail image
				'			<img src="%s" style="max-height:190px" class="img-responsive center-block img-thumbnail">\n' % i['image'] +
				# Paper information
				'			<h3>%s</h3>\n' % i['title'] +
				'			<p>%s. ' % authorlist_to_text(i['author']) +
				'			<em>%s</em><br>\n' % (i['venue'] + ", " + year) +
				'			%s' % (i['comment'] if 'comment' in i else '') +
				'			%s' % (i['github'] if 'github' in i else '') + '</p>\n' +
				# Buttons
				get_button_str_all(i) +
				'		</div>\n')
			if column_cnt == 2 or id == (len(items_international)-1):
				# import ipdb; ipdb.set_trace()
			# just for adding some space - not sure style="height" is compatible for browsers
				f.write(
				# '	<div class="row" style="height: 30px">\n'+
				# '	</div>\n'+						
				'	</div>\n'+
				'</div>\n\n')
			column_cnt += 1
			column_cnt = column_cnt % 3
	f.write('</div>  <!-- end of publication list -->\n\n')
	f.close()


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	write_html('../source/html/publications.html', data)
