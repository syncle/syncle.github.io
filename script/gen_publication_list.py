
class Record:
	def __init__(self, year = '', image='', title='', author='', venue='', pdf='', code='', data='', web='', video='', supp='', comment = '', bibtex=''):
		self.special_year = -1
		self.image = image
		self.title = title
		self.author = author
		self.venue = venue
		self.pdf = pdf
		self.code = code
		self.data = data
		self.web = web
		self.video = video
		self.supp = supp
		self.comment = comment
		self.bibtex = bibtex
	def __str__(self):
		if self.special_year != -1:
			return 'year indicator : %s' % self.special_year
		else:
			return 'image : ' + self.image + '\n' + \
				'title : ' + self.title + '\n' + \
				"author : " + self.author + '\n' + \
				"venue : " + self.venue + '\n' + \
				"pdf : " + self.pdf + '\n' + \
				"code : " + self.code + '\n' + \
				"data : " + self.data + '\n' + \
				"web : " + self.web + '\n' + \
				"video : " + self.video + '\n' + \
				"supp : " + self.supp + '\n' + \
				"comment : " + self.comment + '\n' + \
				"bibtex : " + self.bibtex

def read_record(file):
	f = open(file, "r")
	read = False
	record = Record()
	data = []
	for line in f:
		line = line.rstrip()
		if 'item_start' in line:
			read = True
			continue
		if read:
			if 'special_year=' in line:
				record.special_year = line[13:]
			if 'image=' in line:
				record.image = line[6:]
			if 'title=' in line:
				record.title = line[6:]
			if 'author=' in line:
				record.author = line[7:]
			if 'venue=' in line:
				record.venue = line[6:]
			if 'pdf=' in line:
				record.pdf = line[4:]
			if 'code=' in line:
				record.code = line[5:]
			if 'data=' in line:
				record.data = line[5:]
			if 'web=' in line:
				record.web = line[4:]
			if 'video=' in line:
				record.video = line[6:]
			if 'supp=' in line:
				record.supp = line[5:]
			if 'comment=' in line:
				record.comment = line[8:]
			if 'bibtex=' in line:
				record.bibtex = line[7:]
		if 'item_end' in line:
			data.append(record)
			read = False
			record = Record()
	f.close()
	return data

def get_button_str(link, glyphicon, text):
	return 	'		<a href="%s" target="_blank" class="btn btn-default" role="button">\n' % link + \
			'			<span class="glyphicon glyphicon-%s"></span>' % glyphicon + ' %s\n' % text + \
			'		</a>\n'

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
			button_pdf = ''
			button_code = ''
			button_data = ''
			button_web = ''
			button_video = ''
			button_supp = ''
			button_bibtex = ''
			if data_iter.pdf != '':
				button_pdf = get_button_str(data_iter.pdf, 'file', 'Paper')
			if data_iter.code != '':
				button_code = get_button_str(data_iter.code, 'pencil', 'Code')
			if data_iter.data != '':
				button_data = get_button_str(data_iter.data, 'download-alt', 'Data')
			if data_iter.web != '':
				button_web = get_button_str(data_iter.web, 'home', 'Project Page')
			if data_iter.video != '':
				button_video = get_button_str(data_iter.video, 'play', 'Video')
			if data_iter.supp != '':
				button_supp = get_button_str(data_iter.supp, 'paperclip', 'Supplementary')
			if data_iter.bibtex != '':
				button_bibtex = get_button_str(data_iter.bibtex, 'list', 'Bibtex')

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
					button_pdf + button_code + button_data + button_web + button_video + button_supp + button_bibtex +
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
