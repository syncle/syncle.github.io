
class Record:
	def __init__(self, year = '', image='', title='', author='', venue='', pdf='', code='', data='', web='', video='', supp='', comment = '', bibtex='', executable='', poster='', web_inplace=''):
		self.special_year = -1
		self.image = image
		self.title = title
		self.author = author
		self.venue = venue
		self.pdf = pdf
		self.code = code
		self.data = data
		self.web = web
		self.web_inplace = web_inplace
		self.video = video
		self.supp = supp
		self.comment = comment
		self.bibtex = bibtex
		self.executable = executable
		self.poster = poster
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
				"web_inplace : " + self.web_inplace + '\n' + \
				"video : " + self.video + '\n' + \
				"supp : " + self.supp + '\n' + \
				"comment : " + self.comment + '\n' + \
				"bibtex : " + self.bibtex + '\n' +\
				"executable : " + self.executable + '\n'+\
				"poster : " + self.poster + '\n'

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
			if 'web_inplace=' in line:
				record.web_inplace = line[12:]
			if 'video=' in line:
				record.video = line[6:]
			if 'supp=' in line:
				record.supp = line[5:]
			if 'comment=' in line:
				record.comment = line[8:]
			if 'bibtex=' in line:
				record.bibtex = line[7:]
			if 'executable=' in line:
				record.executable = line[11:]
			if 'poster=' in line:
				record.poster = line[7:]
		if 'item_end' in line:
			data.append(record)
			read = False
			record = Record()
	f.close()
	return data
