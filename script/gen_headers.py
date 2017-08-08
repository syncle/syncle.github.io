
from domain import get_domain

def write_header_html(file, type):
	active_index = ''
	active_about_me = ''
	active_publications = ''
	active_academic_activities = ''
	active_contact = ''
	if type == 'About me':
		active_about_me = 'class="active"'
	elif type == 'Publications':
		active_publications = 'class="active"'
	elif type == 'Academic activities':
		active_academic_activities = 'class="active"'
	elif type == 'Contact':
		active_contact = 'class="active"'
	elif type == "Index":
		active_index = '' # do nothing
	else:
		active_publications = 'class="active"' # project pages for example

	header_str = ''
	if type != 'Index':
		header_str = \
			'<!-- Header -->\n'+\
			'<header>\n'+\
			'	<div class="container" id="maincontent" tabindex="-1">\n'+\
			'		<div class="row">\n'+\
			'			<div class="col-lg-12">\n'+\
			'				<div class="intro-text">\n'+\
			'					<h1>%s</h1>\n' % type +\
			'				</div>\n'+\
			'			</div>\n'+\
			'		</div>\n'+\
			'	</div>\n'+\
			'</header>\n'+\
			'\n'
	if type == 'Publications':
		header_str = \
			'<!-- Header -->\n'+\
			'<header>\n'+\
			'	<div class="container" id="maincontent" tabindex="-1">\n'+\
			'		<div class="row">\n'+\
			'			<div class="col-lg-6 text-left">\n'+\
			'				<div class="intro-text">\n'+\
			'					<h1>%s</h1>\n' % type +\
			'				</div>\n'+\
			'			</div>\n'+\
			'			<div class="col-lg-6 text-right">\n'+\
			'				<div class="intro-text">\n'+\
			'					<br>\n'+\
			'					<a href="https://scholar.google.com/citations?user=_3q6KBIAAAAJ&hl=en" target="_blank" class="btn btn-default" role="button">\n' +\
			'						<span class="glyphicon glyphicon-search"></span> Google Scholar\n'+\
			'					</a>\n'+\
			'					<a href="http://dblp.uni-trier.de/pers/hd/p/Park:Jaesik" target="_blank" class="btn btn-default" role="button">\n'+\
			'						<span class="glyphicon glyphicon-search"></span> DBLP\n'+\
			'					</a>\n'+\
			'				</div>\n'+\
			'			</div>\n'+\
			'		</div>\n'+\
			'	</div>\n'+\
			'</header>\n'+\
			'\n'

	f = open(file, "w")
	f.write(
		'<!-- Navigation -->\n'+
		'<nav id="mainNav" class="navbar navbar-default navbar-fixed-top navbar-custom">\n'+
		'	<div class="container">\n'+
		'		<!-- Brand and toggle get grouped for better mobile display -->\n'+
		'		<div class="navbar-header page-scroll">\n'+
		'			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n'+
		'				<span class="sr-only">Toggle navigation</span> Menu <i class="fa fa-bars"></i>\n'+
		'			</button>\n'+
		'			<a class="navbar-brand" href="%s/index.html">Jaesik Park</a>\n' % get_domain()+
		'		</div>\n'+
		'		<!-- Collect the nav links, forms, and other content for toggling -->\n'+
		'		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n'+
		'			<ul class="nav navbar-nav navbar-right">\n'+
		'				<li class="hidden">\n'+
		'					<a href="%s/index.html"></a>\n' % get_domain()+
		'				</li>\n'+
		'				<li %s>\n' % active_about_me +
		'					<a href="%s/about_me.html">About me</a>\n' % get_domain()+
		'				</li>\n'+
		'				<li %s>\n' % active_publications +
		'					<a href="%s/publications.html">Publications</a>\n' % get_domain()+
		'				</li>\n'+
		'				<li %s>\n' % active_academic_activities +
		'					<a href="%s/academic_activities.html">Academic activities</a>\n' % get_domain()+
		'				</li>\n'+
		'				<li %s>\n' % active_contact +
		'					<a href="%s/contact.html">Contact</a>\n' % get_domain()+
		'				</li>\n'+
		'			</ul>\n'+
		'		</div>\n'+
		'		<!-- /.navbar-collapse -->\n'+
		'	</div>\n'+
		'<!-- /.container-fluid -->\n'+
		'</nav>\n'+
		'\n'+
		header_str +
		'\n'+
		'<div class="container">\n')
