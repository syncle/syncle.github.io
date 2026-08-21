import json
from util import dump_str_to_html_placeholder

def dump_member_info(i, name):
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

def dump_hardware_info(i, name):
	temp = '%s' % ('			<h5><a href="%s" target="_blank">%s</a></h5>\n' % (i['web'], name) if 'web' in i else '			<h5>%s</h5>\n' % name) + \
				'%s' % ('			' + i['comment'] + '<br>\n' if 'comment' in i else '') + \
				'		</div>\n'
	return temp

def write_members(input_path, output_path, data, member_now='yes', autogen='AUTOGEN::Members'):
	dump_str = []
	web = []
	for idx, name in reversed(list(enumerate(data))):
		i = data[name]
		if ('member_now' in i and i['member_now'] == member_now):
			dump_str.append('		<div class="col-md-2 text-center">\n' + 
							'			<img src="%s" class="rounded-circle img-thumbnail shadow mb-2 d-none d-md-block">\n' % i['photo'])
			dump_str.append(dump_member_info(i, name))
	dump_str_to_html_placeholder(input_path, output_path, autogen, dump_str)

def write_hardwares(input_path, output_path, data):
	dump_str = []
	web = []
	for idx, name in list(enumerate(data)):
		i = data[name]
		if ('available_now' in i and i['available_now'] == 'yes'):
			dump_str.append('		<div class="col-md-2 text-center">\n' + 
							'			<img src="%s" class="rounded-circle img-thumbnail shadow mb-2 d-none d-md-block">\n' % i['photo'])
			dump_str.append(dump_hardware_info(i, name))
	dump_str_to_html_placeholder(input_path, output_path, 'AUTOGEN::Hardwares', dump_str)

if __name__ == "__main__":
	with open('../data/students.json') as f:
		data_students = json.load(f)
	with open('../data/hardwares.json') as f:
		data_hardwares = json.load(f)
	
	write_members('../source/html/lab_skeleton.html', '../source/html/lab.html', data_students)
	write_hardwares('../source/html/lab.html', '../source/html/lab.html', data_hardwares)
	write_members('../source/html/lab.html', '../source/html/lab.html', data_students, 'no', 'AUTOGEN::PastMembers')