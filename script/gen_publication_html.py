import json
from util import authorlist_to_html_text
from gen_button import get_button_str_all
from gen_bibtex import get_collapsed_bibtex_html

def write_html(file, data):
	f = open(file, "w")
	# github button
	f.write('<script async defer src="https://buttons.github.io/buttons.js"></script>\n')
	f.write('<div class="container"> <!-- begin of publication list -->\n\n')
	for idx, year in enumerate(data):

		# list up international
		items_international = []
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['language'] == 'international':
						items_international.append(i)
		
		# skip the year if there is no international publication
		if len(items_international) == 0:
			continue
		
		# writing year
		f.write('<div class="container mt-4">\n'+
				'<div class="row">\n'+
				'	<div class="col-lg-12 text-start">\n'+
				'		<h2>%s</h2>\n' % year +
				'	</div>\n'+
				'</div>\n'+
				'</div>\n\n')

		# make a new container
		f.write('<div class="container">\n'+
				'	<div class="row gx-5 gy-4">\n')
		# adding publication elements
		for i in items_international:
			# skip hiding objects
			if 'hide' in i:
				if  i['hide'] == "true":
					continue
			bibtex_button, bibtex_box, nickname = get_collapsed_bibtex_html(i, year)
			# write a html for a paper
			f.write(
				'		<div class="col-lg-4 text-center" id="%s">\n' % nickname +				
				# Thumbnail image
				'			<img src="%s" class="img-fluid rounded float-center img-thumbnail shadow mb-3">\n' % i['image'] + 
				# Paper information
				('			<h4>%s</h4>\n' % i['title'] if len(i['title']) <= 65 else '			<h4 class="em-tight">%s</h4>\n' % i['title']) +
				'			<p class="text-muted">\n' +
				'				%s.\n' % authorlist_to_html_text(i['author']) +
				'				<em>%s</em>\n' % (i['venue'] + ", " + year) +
				'%s' % ('				<br>' + i['comment'] + '\n' if 'comment' in i else '') +
				'%s' % ('				<br>' + i['github'] + '\n' if 'github' in i else '') +
				'			</p>\n' +
				# Buttons
				'			<p>\n' +
				get_button_str_all(i) +	
				bibtex_button + '\n' +
				'			</p>\n' +
				'%s\n' % bibtex_box + 
				'		</div>\n')
		# finish making the container
		f.write(
			'	</div>\n'+
			'</div>\n\n')

		# adding horizontal line
		f.write('<div class="container mt-4">\n'+
				'	<hr class="py-1">\n'+
				'</div>\n\n')
	f.write('</div>  <!-- end of publication list -->\n\n')
	f.close()


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	write_html('../source/html/publications.html', data)
