
from gen_button import get_button_str_all
from record import read_record

def write_html(file, data):
	f = open(file, "w")
	f.write('<div class="container"> <!-- begin of publication list -->\n\n')
	for idx, data_iter in enumerate(data):
		if data_iter.special_year != -1:
			if idx != 0:
				f.write('<hr>\n') # adding horizontal line for every years except for the first appearing year
			# adding year
			f.write('<div class="container">\n'+
					'<div class="row">\n'+
					'	<div class="col-lg-12 text-left">\n'+
					'		<h2 class="name">%s</h2>\n' % data_iter.special_year+
					'	</div>\n'+
					'</div>\n'+
					'</div>\n\n')
		else:
			f.write('<div class="container">\n'+
					'<div class="row">\n'+
					# Thumbnail image
					'	<div class="col-lg-4 col-lg-offset-1">\n'+
					'		<img src="%s" style="max-height:170px" class="img-responsive center-block img-thumbnail">\n' % data_iter.image +
					'	</div>\n'+
					# Paper information
					'	<div class="col-lg-7">\n'+
					'		<h3>%s</h3>\n' % data_iter.title +
					'		<p>%s<br>\n' % data_iter.author +
					'		%s<br>\n' % data_iter.venue +
					'		%s</p>\n' % data_iter.comment +
					# Buttons
					get_button_str_all(data_iter) +
					'	</div>\n'+
					'</div>\n'+
					# just for adding some space - not sure style="height" is compatible for browsers
					'<div class="row" style="height: 30px">\n'+
					'</div>\n'+
					'</div>\n\n')
	f.write('</div>  <!-- end of publication list -->\n\n')
	f.close()

if __name__ == "__main__":
	data = read_record('../publications/publication_data.txt')
	#record = Record('test_title','test_author','test_venue')
	#for data_iter in data:
	#	print(data_iter)

	write_html('../source/publications.html', data)
