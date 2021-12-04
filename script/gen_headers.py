
from domain import get_domain

def write_header_html(file, type):
	active_index = ''
	active_about_me = ''
	active_publications = ''
	active_academic_activities = ''
	active_contact = ''
	active_lab = ''
	if type == 'About me':
		active_about_me = 'active'
	elif type == 'Publications':
		active_publications = 'active'
	elif type == 'Academic activities':
		active_academic_activities = 'active'
	elif type == '@POSTECH':
		active_lab = 'active'
	elif type == 'Contact':
		active_contact = 'active'
	elif type == "Index":
		active_index = '' # do nothing
	else:
		active_publications = 'class="active"' # project pages for example

	header_str = ''
	if type != 'Index':
		header_str = \
			'<header class="masthead bg-primary text-white test-start">\n'+\
			'	<div class="container d-flex align-items-left flex-column">\n'+\
			'		<h1 class="text-uppercase mb-0">%s</h1>\n' % type+\
			'	</div>\n'+\
			'</header>\n'+\
			'\n'
	if type == 'Publications':
		header_str = \
			'<header class="masthead bg-primary text-white">\n'+\
			'	<div class="container">\n'+\
			'		<div class="row">\n'+\
			'			<div class="col-lg-6 text-start">\n'+\
			'				<h1 class="text-uppercase mb-0">%s</h1>\n' % type +\
			'			</div>\n'+\
			'			<div class="col-lg-6 text-end">\n'+\
			'				<a href="https://scholar.google.com/citations?user=_3q6KBIAAAAJ&hl=en" target="_blank" class="btn btn-default" role="button">\n' +\
			'					<span class="glyphicon glyphicon-search"></span> Google Scholar\n'+\
			'				</a>\n'+\
			'				<a href="http://dblp.uni-trier.de/pers/hd/p/Park:Jaesik" target="_blank" class="btn btn-default" role="button">\n'+\
			'					<span class="glyphicon glyphicon-search"></span> DBLP\n'+\
			'				</a>\n'+\
			'			</div>\n'+\
			'		</div>\n'+\
			'	</div>\n'+\
			'</header>\n'+\
			'\n'		

	f = open(file, "w")
	f.write(
		'<nav class="navbar navbar-expand-lg bg-secondary fixed-top text-uppercase" id="mainNav">\n' +
		'	<div class="container">\n' +
		'		<a class="navbar-brand" href="%s">Jaesik Park</a>\n' % get_domain()+
		'		<button class="navbar-toggler font-weight-bold bg-primary text-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">\n' +
		'			Menu\n' +
		'			<i class="fas fa-bars"></i>\n' +
		'		</button>\n' +
		'		<div class="collapse navbar-collapse" id="navbarResponsive">\n' +
		'			<ul class="navbar-nav ms-auto">\n' +
		'				<li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3" href="%s"></a></li>\n' % get_domain()+
		'				<li class="nav-item mx-0 mx-lg-1"><a class="nav-link %s py-3 px-0 px-lg-3" href="%s/about_me">About me</a></li>\n' % (active_about_me, get_domain())+
		'				<li class="nav-item mx-0 mx-lg-1"><a class="nav-link %s py-3 px-0 px-lg-3" href="%s/academic_activities">Academic activities</a></li>\n' % (active_academic_activities, get_domain())+
		'				<li class="nav-item mx-0 mx-lg-1"><a class="nav-link %s py-3 px-0 px-lg-3" href="%s/publications">Publications</a></li>\n' % (active_publications, get_domain())+
		'				<li class="nav-item mx-0 mx-lg-1"><a class="nav-link %s py-3 px-0 px-lg-3" href="%s/lab">@POSTECH</a></li>\n' % (active_lab, get_domain())+
		'				<li class="nav-item mx-0 mx-lg-1"><a class="nav-link %s py-3 px-0 px-lg-3" href="%s/contact">Contact</a></li>\n' % (active_contact, get_domain())+
		'			</ul>\n' +
		'		</div>\n' +
		'	</div>\n' +
		'</nav>\n' +
		'\n'+
		header_str +
		'\n')
