import json
from util import authorlist_to_html_text
from gen_button import get_button_str_all
from gen_bibtex import get_collapsed_bibtex_html

def write_news(file, data):

	f = open(file, "w")

	# before news
	f.write('<div class="container mt-4">\n'+
			'	<div class="row gx-4 gy-4">\n'+
			'		<div class="col-lg-12 text-start">\n'+
			'			<h3><br></h3>\n'+
			'			<h3><br></h3>\n'+
			'		</div>\n'+
			'		<div class="col-lg-3">\n'+
			'			<img src="source/images/jaesik-park.jpg" class="shadow rounded-circle img-thumbnail">\n'+
			'		</div>\n'+
			'		<div class="col-lg-9">\n'+
			'			<h1>Jaesik Park</h1>\n'+
			'			<ul class="list-group mb-4 shadow-sm">\n'+
			'				<li class="list-group-item">\n'+
			'					<p class="lead">Hello! I am an Assistant Professor at POSTECH.\n'+
			'					I am looking for self-motivated students to make <a href="http://cvlab.postech.ac.kr" target="_blank">POSTECH computer vision lab</a> together.\n'+
			'					Please <a href="http://jaesik.info/contact">apply our lab</a> if interested.</p>\n'+
			'				</li>\n'+
			'			</ul>\n')
	
	# recent K items
	f.write('			<h2>News</h2>\n'+
			'			<ul class="list-group shadow-sm">\n')
	K = 6
	for record in data[:K]:
		f.write('				<li class="list-group-item">\n' +
				'					%s\n' % record + 
				'				</li>\n')
	f.write('			</ul>\n')

	# other items
	f.write('			<p>\n'+
			'				<button class="btn btn-outline-secondary shadow-sm" type="button" data-bs-toggle="collapse" data-bs-target="#previousNews" aria-expanded="false" aria-controls="previousNews">\n'+
			'					Previous &#9661;\n'+
			'				</button>\n'+
			'			</p>\n'+
			'			<div class="collapse" id="previousNews">\n'+
			'				<ul class="list-group shadow-sm">\n')
	for record in data[K:]:
		f.write('					<li class="list-group-item">\n'+
				'						%s\n' % record +
				'					</li>\n')

	# after news
	f.write('				</ul>\n'+
			'			</div>\n'+
			'		</div>\n'+
			'	</div>\n'+
			'</div>\n')

if __name__ == "__main__":
	with open('../data/news.html') as f:
		data = f.read().splitlines()
	
	write_news('../source/html/index.html', data)
