from gen_headers import write_header_html
# from record import read_record
from gen_button_for_project_page import append_button_html
import os
import json
from util import clear_file, include_file

path_header = '../source/html/header.html'
path_footer = '../source/html/footer.html'

def gen_project_page(path, title):
	clear_file('../' + path + 'index.html')
	include_file('../' + path + 'index.html', path_header)
	write_header_html('../' + path + 'content_header.html', title)
	include_file('../' + path + 'index.html', '../' + path + 'content_header.html')
	include_file('../' + path + 'index.html', '../' + path + 'content_index.html')
	with open('../' + path + 'record.json') as f:
		data = json.load(f)
	append_button_html('../' + path + 'index.html', data)
	include_file('../' + path + 'index.html', path_footer)

def gen_page(page, type):
	clear_file('../%s.html' % page)
	include_file('../%s.html' % page, path_header)
	write_header_html('../source/html/%s_header.html' % page, type)
	include_file('../%s.html' % page, '../source/html/%s_header.html' % page)
	include_file('../%s.html' % page, '../source/html/%s.html' % page)
	include_file('../%s.html' % page, path_footer)
	os.remove('../source/html/%s_header.html' % page)
	if page == 'publications':
		os.remove('../source/html/%s.html' % page)

if __name__ == "__main__":
	gen_page('index', 'Index')
	os.remove('../source/html/index.html')
	
	# publications
	gen_page('publications', 'Publications')	
	gen_project_page('publications/identigram/', 'Identigram/Watermark Removal')
	gen_project_page('publications/lightcalib/', 'Calibrating a Non-isotropic Near Point Light Source')
	gen_project_page('publications/photoconsistency/', 'Color Consistency for Community Photo Collections')
	gen_project_page('publications/depthups/', 'High Quality Depth Map Upsampling')
	gen_project_page('publications/multiviewps/', 'Multiview Photometric Stereo')

	gen_page('lab', "Lab")
	os.remove('../source/html/lab.html')
	gen_page('contact', 'Contact')
