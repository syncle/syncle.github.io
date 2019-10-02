from gen_headers import write_header_html
from record import read_record
from gen_button_for_project_page import append_button_html
import os

path_header = '../source/header.html'
path_footer = '../source/footer.html'

def clear_file(file):
	f = open(file, "w")
	f.close()

def include_file(output_file, include_file):
	f = open(include_file, "r")
	copy = open(output_file, "a")
	for line in f:
		copy.write(line)
	f.close()
	copy.close()

def gen_project_page(path, title):
	clear_file('../' + path + 'index.html')
	include_file('../' + path + 'index.html', path_header)
	write_header_html('../' + path + 'header.html', title)
	include_file('../' + path + 'index.html', '../' + path + 'content_header.html')
	include_file('../' + path + 'index.html', '../' + path + 'content_index.html')
	record = read_record('../' + path + 'publication_data.txt')
	#print(record[0])
	append_button_html('../' + path + 'index.html', record)
	#include_file(path + '/index.html', '../source/publications_footer.html')
	include_file('../' + path + 'index.html', path_footer)

def gen_page(page, type):
	clear_file('../%s.html' % page)
	include_file('../%s.html' % page, path_header)
	write_header_html('../source/%s_header.html' % page, type)
	include_file('../%s.html' % page, '../source/%s_header.html' % page)
	include_file('../%s.html' % page, '../source/%s.html' % page)
	include_file('../%s.html' % page, path_footer)
	os.remove('../source/%s_header.html' % page)
	if page == 'publications':
		os.remove('../source/%s.html' % page)

if __name__ == "__main__":
	gen_page('index', 'Index')
	gen_page('about_me', 'About me')
	gen_page('academic_activities', 'Academic activities')

	# publications
	gen_page('publications', 'Publications')
	gen_project_page('publications/identigram/', 'Identigram/Watermark Removal')
	gen_project_page('publications/lightcalib/', 'Calibrating a Non-isotropic Near Point Light Source')
	gen_project_page('publications/photoconsistency/', 'Color Consistency for Community Photo Collections')
	gen_project_page('publications/depthups/', 'High Quality Depth Map Upsampling')
	gen_project_page('publications/multiviewps/', 'Multiview Photometric Stereo')

	gen_page('lab', "@POSTECH")
	gen_page('contact', 'Contact')
