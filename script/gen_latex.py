import json
from gen_button import get_button_str_all
from util import *

def write_latex_publication(file, data):
	f = open(file, "w")
	f.write('\\section{Publications}\n')
	f.write('\\resumePublicationListStart\n')
	# import ipdb; ipdb.set_trace()
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['type'] == 'international':
						f.write('\publicationItem' + \
						'{' + change_bold(authorlist_to_text(i['author'])) + '}' + \
						'{' + i['title'] + '}' + \
						'{' + change_bold(i['venue']) + '}\n' \
						)
	f.write('\\resumePublicationListEnd\n')
	f.close()

def write_latex_awards(file, data):
	f = open(file, "w")
	f.write('\\section{Awards}\n')
	f.write('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'awards':
				for i in items:
					if not 'hide' in i:
						f.write('\\resumeItem' + \
						'{' + i['title'] + ', ' \
							+ i['awardee'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ number_to_month(i['month']) + ' ' + year + '}\n')
	f.write('\\resumeItemListEnd\n')
	f.close()

if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	write_latex_publication('../source/latex/publication.tex', data)
	write_latex_awards('../source/latex/awards.tex', data)

	page = 'cv'
	clear_file('../%s.tex' % page)
	include_file('../%s.tex' % page, '../source/latex/header.tex')
	include_file('../%s.tex' % page, '../source/latex/publication.tex')
	include_file('../%s.tex' % page, '../source/latex/awards.tex')
	include_file('../%s.tex' % page, '../source/latex/footer.tex')
