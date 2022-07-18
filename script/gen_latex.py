import json
import os
from gen_button import get_button_str_all
from util import *

def get_venue(i, year):
	v = change_html_bold_to_latex_bold(i['venue']) 
	v += ', '
	v += (number_to_month(i['month']) + ' ' if 'month' in i else '')
	v += year
	return v

def write_latex_publication(file, data):
	f = open(file, "w")
	f.write('\\section{Publications}\n\n')
	f.write('International\n')
	f.write('\\resumePublicationListStart\n')
	# international
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['language'] == 'international':
						f.write('    \publicationItem' + \
						'{' + change_html_bold_to_latex_bold(authorlist_to_html_text(i['author'])) + '}' + \
						'{' + i['title'] + '}' + \
						'{' + get_venue(i, year) + '}' + \
						'{' + (change_percent(change_html_bold_to_latex_bold(i['comment'])) if 'comment' in i else '') + '}\n')
	f.write('\\resumePublicationListEnd\n\n\n\n')
	# domestic
	f.write('Domestic\n')
	f.write('\\resumePublicationListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['language'] == 'domestic':
						f.write('    \publicationItem' + \
						'{' + change_html_bold_to_latex_bold(authorlist_to_html_text(i['author'])) + '}' + \
						'{' + i['title'] + '}' + \
						'{' + get_venue(i, year) + '}' + \
						'{' + (change_percent(change_html_bold_to_latex_bold(i['comment'])) if 'comment' in i else '') + '}\n')
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
						'{' + change_html_bold_to_latex_bold(i['title']) + ', ' \
							+ i['awardee'] + ', ' \
							+ (change_emph(i['comment'])  + ', ' if 'comment' in i else '') \
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
						'{' + i['title'] \
							+ (', ' + i['comment'] if 'comment' in i else '') \
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
						'{\\textit{' + i['title'] + '}, ' \
							+ i['venue'] + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ number_to_month(i['month']) + ' ' + year + '}\n')
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()


def write_latex_funding(file, data):
	f = open(file, "w")
	f.write('\\section{Funding}\n')
	f.write('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'funding':
				for i in items:
					f.write('    \\resumeItem' + \
					'{\\textit{' + i['title'] + '}, ' \
						+ i['source'] + ', ' \
						+ i['period'] \
						+ (',' + i['comment']  if 'comment' in i else '') + '}\n')
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
							+ (change_html_bold_to_latex_bold(i['comment'])  + ', ' if 'comment' in i else '') \
							+ i['semester'] + ', ' + ' ' + year + '}\n')
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
						'{' + change_html_bold_to_latex_bold(i['title']) + ', ' \
							+ change_html_bold_to_latex_bold(i['venue']) + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ ' ' + year + '}\n')
	f.write(change_html_bold_to_latex_bold('\\resumeItem{Have been served as a reviewer for international conferences, such as <b>CVPR</b>, <b>ICCV</b>, <b>ECCV</b>, <b>ICLR</b>, <b>NeurIPS</b>, <b>AAAI</b>, <b>ICRA</b>, <b>IROS</b>, <b>SIGGRAPH</b>, <b>SIGGRAPH Asia</b>, BMVC, 3DV, ACCV, WACV, and so on.}\n'))
	f.write(change_html_bold_to_latex_bold('\\resumeItem{Have been served as a reviewer for international journals, such as <b>TPAMI</b>, <b>TIP</b>, <b>TVCG</b>, <b>TRO</b>, <b>IJCV</b>, CVIU, SPL, IVC, Neurocomputing, and so on.}\n'))
	f.write('\\resumeItemListEnd\n\n\n\n')
	f.close()


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	source_path = '/source/latex'

	write_latex_publication('..%s/publication.tex' % source_path, data)
	write_latex_awards('..%s/awards.tex' % source_path, data)
	write_latex_patents('..%s/patents.tex' % source_path, data)
	write_latex_teaching('..%s/teaching.tex' % source_path, data)
	write_latex_funding('..%s/funding.tex' % source_path, data)
	write_latex_talks('..%s/talks.tex' % source_path, data)
	write_latex_program_committe('..%s/program_committe.tex' % source_path, data)

	page = 'cv'
	clear_file('..%s/%s.tex' % (source_path, page))
	include_file('..%s/%s.tex' % (source_path, page), '..%s/header.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/publication.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/program_committe.tex' % source_path )
	include_file('..%s/%s.tex' % (source_path, page), '..%s/awards.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/patents.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/teaching.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/funding.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/talks.tex' % source_path)
	include_file('..%s/%s.tex' % (source_path, page), '..%s/footer.tex' % source_path)

	os.remove('..%s/publication.tex' % source_path)
	os.remove('..%s/awards.tex' % source_path)
	os.remove('..%s/patents.tex' % source_path)
	os.remove('..%s/teaching.tex' % source_path)
	os.remove('..%s/funding.tex' % source_path)
	os.remove('..%s/talks.tex' % source_path)
	os.remove('..%s/program_committe.tex' % source_path)

	if not os.path.exists('..%s/build' %  source_path):
		os.mkdir('..%s/build' %  source_path)
