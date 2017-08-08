from gen_headers import write_header_html
from record import read_record
from gen_button_for_project_page import append_button_html

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
	clear_file(path + '/index.html')
	include_file(path + '/index.html', path_header)
	write_header_html(path + '/content_header.html', title)
	include_file(path + '/index.html', path + '/content_header.html')
	include_file(path + '/index.html', path + '/content_index.html')
	record = read_record(path + '/publication_data.txt')
	print(record[0])
	append_button_html(path + '/index.html', record)
	include_file(path + '/index.html', '../source/content_publications_footer.html')
	include_file(path + '/index.html', path_footer)

if __name__ == "__main__":

	# index_html
	clear_file('../index.html')
	include_file('../index.html', path_header)
	write_header_html('../source/content_header_index.html', 'Index')
	include_file('../index.html', '../source/content_header_index.html')
	include_file('../index.html', '../source/content_index.html')
	include_file('../index.html', path_footer)

	# publications_html
	clear_file('../publications.html')
	include_file('../publications.html', path_header)
	write_header_html('../source/content_header_publications.html', 'Publications')
	include_file('../publications.html', '../source/content_header_publications.html')
	include_file('../publications.html', '../source/content_publications_middle.html')
	include_file('../publications.html', '../source/content_publications_footer.html')
	include_file('../publications.html', path_footer)

	gen_project_page('../publications/identigram', 'Identigram/Watermark Removal')
	gen_project_page('../publications/lightcalib', 'Calibrating a Non-isotropic Near Point Light Source')
	gen_project_page('../publications/photoconsistency', 'Color Consistency for Community Photo Collections')
	gen_project_page('../publications/depthups', 'High Quality Depth Map Upsampling')
	gen_project_page('../publications/multiviewps', 'Multiview Photometric Stereo')

	# about_me_html
	clear_file('../about_me.html')
	include_file('../about_me.html', path_header)
	write_header_html('../source/content_header_about_me.html', 'About me')
	include_file('../about_me.html', '../source/content_header_about_me.html')
	include_file('../about_me.html', '../source/content_about_me.html')
	include_file('../about_me.html', path_footer)

	# academic_activities_html
	clear_file('../academic_activities.html')
	include_file('../academic_activities.html', path_header)
	write_header_html('../source/content_header_academic_activities.html', 'Academic activities')
	include_file('../academic_activities.html', '../source/content_header_academic_activities.html')
	include_file('../academic_activities.html', '../source/content_academic_activities.html')
	include_file('../academic_activities.html', path_footer)

	# academic_activities_html
	clear_file('../contact.html')
	include_file('../contact.html', path_header)
	write_header_html('../source/content_header_contact.html', 'Contact')
	include_file('../contact.html', '../source/content_header_contact.html')
	include_file('../contact.html', '../source/content_contact.html')
	include_file('../contact.html', path_footer)
