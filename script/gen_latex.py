import json
import os
from gen_button import get_button_str_all
from domain import get_full_html_path
from util import *

def get_venue(i, year):
	v = change_html_bold_to_latex_bold(i['venue']) 
	v += ', '
	v += (number_to_month(i['month']) + ' ' if 'month' in i else '')
	v += year
	return v

def get_latex_publication(data):
	dump_str = []
	dump_str.append('\\section{Publications}\n\n')
	dump_str.append('International\n')
	dump_str.append('\\resumePublicationListStart\n')
	# international
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['language'] == 'international':
						dump_str.append('    \publicationItem' + \
						'{' + change_html_bold_to_latex_bold(authorlist_to_html_text(i['author'])) + '}' + \
						'{' + ('\href{' + get_full_html_path(i['pdf']) + '}{' + i['title'] + '}' if 'pdf' in i else i['title']) + '}' + \
						'{' + get_venue(i, year) + '}' + \
						'{' + (change_percent(change_html_bold_to_latex_bold(i['comment'])) if 'comment' in i else '') + '}\n')
	dump_str.append('\\resumePublicationListEnd\n\n\n\n')
	# domestic
	dump_str.append('Domestic\n')
	dump_str.append('\\resumePublicationListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'papers':
				for i in items:
					if i['language'] == 'domestic':
						dump_str.append('    \publicationItem' + \
						'{' + change_html_bold_to_latex_bold(authorlist_to_html_text(i['author'])) + '}' + \
						'{' + i['title'] + '}' + \
						'{' + get_venue(i, year) + '}' + \
						'{' + (change_percent(change_html_bold_to_latex_bold(i['comment'])) if 'comment' in i else '') + '}\n')
	dump_str.append('\\resumePublicationListEnd\n\n\n\n')
	return dump_str


def get_latex_awards(data):
	dump_str = []
	dump_str.append('\\section{Awards}\n')
	dump_str.append('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'awards':
				for i in items:
					if not 'hide' in i:
						dump_str.append('    \\resumeItem' + \
						'{' + change_html_bold_to_latex_bold(i['title']) + ', ' \
							+ i['awardee'] + ', ' \
							+ (change_emph(i['comment'])  + ', ' if 'comment' in i else '') \
							+ number_to_month(i['month']) + ' ' + year + '}\n')
	dump_str.append('\\resumeItemListEnd\n\n\n\n')
	return dump_str


def get_latex_patents(data):
	dump_str = []
	dump_str.append('\\section{Patents}\n')
	dump_str.append('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'patents':
				for i in items:
					if not 'hide' in i:
						dump_str.append('    \\resumeItem' + \
						'{' + i['title'] \
							+ (', ' + i['comment'] if 'comment' in i else '') \
							+ '}\n')
	dump_str.append('\\resumeItemListEnd\n\n\n\n')
	return dump_str


def get_latex_talks(data):
	dump_str = []
	dump_str.append('\\section{Talks}\n')
	dump_str.append('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'talks':
				for i in items:
					if not 'hide' in i:
						dump_str.append('    \\resumeItem' + \
						'{\\textit{' + i['title'] + '}, ' \
							+ change_html_bold_to_latex_bold(i['venue']) + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ number_to_month(i['month']) + ' ' + year + '}\n')
	dump_str.append('\\resumeItemListEnd\n\n\n\n')
	return dump_str


def get_latex_funding(data):
	dump_str = []
	dump_str.append('\\section{Funding}\n')
	dump_str.append('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'funding':
				for i in items:
					dump_str.append('    \\resumeItem' + \
					'{\\textit{' + i['title'] + '}, ' \
						+ i['source'] + ', ' \
						+ i['period'] \
						+ (',' + i['comment']  if 'comment' in i else '') + '}\n')
	dump_str.append('\\resumeItemListEnd\n\n\n\n')
	return dump_str


def get_latex_teaching(data):
	dump_str = []
	dump_str.append('\\section{Teaching}\n')
	dump_str.append('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'teaching':
				for i in items:
					if not 'hide' in i:
						dump_str.append('    \\resumeItem' + \
						'{' + i['title'] + ', ' \
							+ (change_html_bold_to_latex_bold(i['comment'])  + ', ' if 'comment' in i else '') \
							+ i['semester'] + ', ' + ' ' + year + '}\n')
	dump_str.append('\\resumeItemListEnd\n\n\n\n')
	return dump_str
	

def get_latex_program_committe(data):
	dump_str = []
	dump_str.append('\\section{Program Committee}\n')
	dump_str.append('\\resumeItemListStart\n')
	for year in data:
		for category, items in data[year].items():
			if category == 'program committee':
				for i in items:
					if not 'hide' in i:
						dump_str.append('    \\resumeItem' + \
						'{' + change_html_bold_to_latex_bold(i['title']) + ', ' \
							+ change_html_bold_to_latex_bold(i['venue']) + ', ' \
							+ (i['comment']  + ', ' if 'comment' in i else '') \
							+ ' ' + year + '}\n')
	dump_str.append(change_html_bold_to_latex_bold('\\resumeItem{Have been served as a reviewer for international conferences, such as <b>CVPR</b>, <b>ICCV</b>, <b>ECCV</b>, <b>ICLR</b>, <b>NeurIPS</b>, <b>AAAI</b>, <b>ICRA</b>, <b>IROS</b>, <b>SIGGRAPH</b>, <b>SIGGRAPH Asia</b>, BMVC, 3DV, ACCV, WACV, and so on.}\n'))
	dump_str.append(change_html_bold_to_latex_bold('\\resumeItem{Have been served as a reviewer for international journals, such as <b>TPAMI</b>, <b>TIP</b>, <b>TVCG</b>, <b>TRO</b>, <b>IJCV</b>, CVIU, SPL, IVC, Neurocomputing, and so on.}\n'))
	dump_str.append('\\resumeItemListEnd\n\n\n\n')
	return dump_str


if __name__ == "__main__":
	with open('../data/record.json') as f:
		data = json.load(f)
	
	if not os.path.exists('../source/latex/build'):
		os.mkdir('../source/latex/build')
	
	source_path = '../source/latex/cv_skeleton.tex'
	output_path = '../source/latex/cv.tex'

	dump_str_to_html_placeholder(source_path, output_path,
				'AutoGen::publication', get_latex_publication(data))
	dump_str_to_html_placeholder(output_path, output_path,
				'AutoGen::program_committe', get_latex_program_committe(data))
	dump_str_to_html_placeholder(output_path, output_path,
				'AutoGen::awards', get_latex_awards(data))
	dump_str_to_html_placeholder(output_path, output_path,
				'AutoGen::patents', get_latex_patents(data))
	dump_str_to_html_placeholder(output_path, output_path,
				'AutoGen::teaching', get_latex_teaching(data))
	dump_str_to_html_placeholder(output_path, output_path,
				'AutoGen::funding', get_latex_funding(data))
	dump_str_to_html_placeholder(output_path, output_path,
				'AutoGen::talks', get_latex_talks(data))
