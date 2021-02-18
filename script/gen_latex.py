import json
from gen_button import get_button_str_all
from util import *

def write_latex_publication(file, data):
	f = open(file, "w")
	f.write('\\section{Publications}\n\n\n\n')
	f.write('International\n')
	f.write('\\resumePublicationListStart\n')
	# international
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['type'] == 'international':
						f.write('    \publicationItem' + \
						'{' + change_bold(authorlist_to_text(i['author'])) + '}' + \
						'{' + i['title'] + '}' + \
						'{' + change_bold(i['venue']) + '}\n' \
						)
	f.write('\\resumePublicationListEnd\n\n\n\n')
	# domestic
	f.write('Domestic\n')
	f.write('\\resumePublicationListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['type'] == 'domestic':
						f.write('    \publicationItem' + \
						'{' + change_bold(authorlist_to_text(i['author'])) + '}' + \
						'{' + i['title'] + '}' + \
						'{' + change_bold(i['venue']) + '}\n' \
						)
	f.write('\\resumePublicationListEnd\n\n\n\n')
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
						f.write('    \\resumeItem' + \
						'{' + i['title'] + ', ' \
							+ i['awardee'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ number_to_month(i['month']) + ' ' + year + '}\n')
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()


def write_latex_patents(file, data):
	f = open(file, "w")
	f.write('\\section{Patents}\n')
	f.write('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'patents':
				for i in items:
					if not 'hide' in i:
						f.write('    \\resumeItem' + \
						'{' + i['title'] + ', ' \
							# + i['awardee'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ '}\n')
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()


def write_latex_talks(file, data):
	f = open(file, "w")
	f.write('\\section{Talks}\n')
	f.write('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'talks':
				for i in items:
					if not 'hide' in i:
						f.write('    \\resumeItem' + \
						'{' + i['title'] + ', ' \
							+ i['venue'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ number_to_month(i['month']) + ' ' + year + '}\n')
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()


def write_latex_teaching(file, data):
	f = open(file, "w")
	f.write('\\section{Teaching}\n')
	f.write('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'teaching':
				for i in items:
					if not 'hide' in i:
						f.write('    \\resumeItem' + \
						'{' + i['title'] + ', ' \
							+ i['semester'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ ' ' + year + '}\n')
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()
	

def write_latex_program_committe(file, data):
	f = open(file, "w")
	f.write('\\section{Program Committee}\n')
	f.write('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'program committee':
				for i in items:
					if not 'hide' in i:
						f.write('    \\resumeItem' + \
						'{' + i['title'] + ', ' \
							+ i['venue'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ ' ' + year + '}\n')
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	write_latex_publication('../source/latex/publication.tex', data)
	write_latex_awards('../source/latex/awards.tex', data)
	write_latex_patents('../source/latex/patents.tex', data)
	write_latex_teaching('../source/latex/teaching.tex', data)
	write_latex_talks('../source/latex/talks.tex', data)
	write_latex_program_committe('../source/latex/program_committe.tex', data)

	page = 'cv'
	clear_file('../%s.tex' % page)
	include_file('../%s.tex' % page, '../source/latex/header.tex')
	include_file('../%s.tex' % page, '../source/latex/publication.tex')
	include_file('../%s.tex' % page, '../source/latex/program_committe.tex')
	include_file('../%s.tex' % page, '../source/latex/awards.tex')
	include_file('../%s.tex' % page, '../source/latex/patents.tex')
	include_file('../%s.tex' % page, '../source/latex/teaching.tex')
	include_file('../%s.tex' % page, '../source/latex/talks.tex')
	include_file('../%s.tex' % page, '../source/latex/footer.tex')
