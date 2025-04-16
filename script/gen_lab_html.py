import json
from util import dump_str_to_html_placeholder

def dump_other_info(i, name):
	temp = '%s' % ('			<h5><a href="%s" target="_blank">%s</a></h5>\n' % (i['web'], name) if 'web' in i else '			<h5>%s</h5>\n' % name) + \
				'%s' % ('			' + i['ms_start'] if 'ms_start' in i else '') + \
				'%s' % (' - ' + i['ms_end'] + '<br>\n' if 'ms_end' in i else '') + \
				'%s' % ('			' + i['ms_comment'] + '<br>\n' if 'ms_comment' in i else '') + \
				'%s' % ('			' + i['phd_start'] if 'phd_start' in i else '') + \
				'%s' % (' - ' + i['phd_end'] + '<br>\n' if 'phd_end' in i else '') + \
				'%s' % ('			' + i['phd_comment'] + '<br>\n' if 'phd_comment' in i else '') + \
				'%s' % ('			' + i['int_start'] if 'int_start' in i else '') + \
				'%s' % (' - ' + i['int_end'] + '<br>\n' if 'int_end' in i else '') + \
				'%s' % ('			' + i['int_comment'] + '<br>\n' if 'int_comment' in i else '') + \
				'%s' % ('			' + i['visit_period'] + '<br>\n' if 'visit_period' in i else '') + \
				'%s' % ('			' + i['visit_comment'] + '<br>\n' if 'visit_comment' in i else '') + \
				'%s' % ('			' + i['job'] + '<br>\n' if 'job' in i else '') + \
				'		</div>\n'
	return temp

def write_members(input_path, output_path, data):
	dump_str = []
	web = []
	for idx, name in reversed(list(enumerate(data))):
		i = data[name]
		if ('member_now' in i and i['member_now'] == 'yes'):
			dump_str.append('		<div class="col-md-3 text-center">\n' + 
							'			<img src="%s" class="rounded-circle img-thumbnail shadow mb-3 d-none d-md-block">\n' % i['photo'])
			dump_str.append(dump_other_info(i, name))
	dump_str_to_html_placeholder(input_path, output_path, 'AUTOGEN::Members', dump_str)

def write_past_members(input_path, output_path, data):
	dump_str = []
	web = []
	for idx, name in enumerate(data):
		i = data[name]
		if ('member_now' not in i or i['member_now'] != 'yes'):
			dump_str.append('		<div class="col-md-2 text-center">\n' + 
							'			<img src="%s" class="rounded-circle img-thumbnail shadow mb-2 d-none d-md-block">\n' % i['photo'])
			dump_str.append(dump_other_info(i, name))
	dump_str_to_html_placeholder(input_path, output_path, 'AUTOGEN::PastMembers', dump_str)

if __name__ == "__main__":
	with open('../data/students.json') as f:
		data = json.load(f)
	
	write_members('../source/html/lab_skeleton.html', '../source/html/lab.html', data)
	write_past_members('../source/html/lab.html', '../source/html/lab.html', data)