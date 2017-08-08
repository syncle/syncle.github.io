
from gen_button import get_button_str_all
from record import read_record

def write_html(file, data):
	f = open(file, "w")
	for data_iter in data:
		if data_iter.special_year != -1:
			f.write('<div class="container">\n'+
					'	<div class="row">\n'+
					'		<div class="col-lg-12 text-left">\n'+
					'			<h2 class="name">%s</h2>\n' % data_iter.special_year+
					'		</div>\n'+
					'	</div>\n'+
					'</div>\n\n')
		else:
			button = get_button_str_all(data_iter)
			f.write(
					'<div class="row">\n'+
					# Image
					'	<div class="col-lg-4 col-lg-offset-1">\n'+
					'		<img src="%s" style="max-height:170px" class="img-responsive center-block">\n' % data_iter.image +
					'	</div>\n'+
					# Paper information
					'	<div class="col-lg-7">\n'+
					'		<h3>%s</h3>\n' % data_iter.title +
					'		<p>%s<br>\n' % data_iter.author +
					'		%s<br>\n' % data_iter.venue +
					'		%s</p>\n' % data_iter.comment +
					# Buttons
					button +
					# Some stupid spacing
					'		<p><br></p>\n'+
					'	</div>\n'+
					'</div>\n\n')
	f.close()

if __name__ == "__main__":
	data = read_record('../publications/publication_data.txt')
	#record = Record('test_title','test_author','test_venue')
	for data_iter in data:
		print(data_iter)

	write_html('../source/content_publications_middle.html', data)
