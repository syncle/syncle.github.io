import json
from util import authorlist_to_html_text, dump_str_to_html_placeholder
from gen_button import get_button_str_all
from gen_bibtex import get_collapsed_bibtex_html

def write_news(input_path, output_path, data):

	dump_str = []

	# recent items
	K = 6
	for record in data[:K]:
		dump_str.append('				<li class="list-group-item">\n' +
						'					%s\n' % record + 
						'				</li>\n')
	
	dump_str_to_html_placeholder(input_path, output_path, 'AUTOGEN::Recent', dump_str)

	# other items
	dump_str.clear()
	for record in data[K:]:
		dump_str.append('					<li class="list-group-item">\n'+
						'						%s\n' % record +
						'					</li>\n')
	dump_str_to_html_placeholder(output_path, output_path, 'AUTOGEN::Others', dump_str)

if __name__ == "__main__":

	# read raw data
	with open('../data/news.html') as f:
		data = f.read().splitlines()
	
	write_news('../source/html/index_skeleton.html',
			'../source/html/index.html',
			data)