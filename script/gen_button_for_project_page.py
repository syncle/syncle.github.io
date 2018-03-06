
from gen_button import get_button_str_all
from record import read_record

def append_button_html(path, filename, data):
	f = open('../' + path + filename, "a")
	f.write(# Buttons
			'<div class="col-lg-8 col-lg-offset-2">\n'+
			'	<h2>Publication(s)</h2>\n')
	for data_iter in data:
		f.write(
				# Paper information
				'		<h3>%s</h3>\n' % data_iter.title +
				'		<p>%s<br>\n' % data_iter.author +
				'		%s<br>\n' % data_iter.venue +
				'		%s</p>\n' % data_iter.comment +
				# Buttons
				get_button_str_all(data_iter, path) +
				# Some stupid spacing
				'		<p><br></p>\n')
	f.write('</div>\n\n')
	f.close()
