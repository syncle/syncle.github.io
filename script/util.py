from cgitb import html

def dump_str_to_html_placeholder(input_path, output_path, placeholder_id, dump_str):	
	with open(input_path, 'r') as f:
		html_data = f.readlines()
	# split data before and after the placeholder_id
	split1 = []
	split2 = []
	found = False
	for html_line in html_data:		
		if placeholder_id in html_line:
			found = True
			continue
		if not found:
			split1.append(html_line)
		else:
			split2.append(html_line)
	if not found:
		return 1
	# make new file
	with open(output_path, 'w') as f:
		f.writelines(split1)
		f.writelines(dump_str)
		f.writelines(split2)
	return 0

def number_to_month(m):
    switcher = {
        1: "Jan.",
        2: "Feb.",
        3: "March",
        4: "Apr.",
        5: "May",
        6: "June",
        7: "July",
        8: "Aug.",
        9: "Sep.",
        10: "Oct.",
        11: "Nov.",
        12: "Dec."
    }
    return switcher.get(m, "Invalid")


def authorlist_to_html_text(author):
	# bold my name
	for idx, a in enumerate(author):
		author[idx] = a.replace('Jaesik Park', '<b>Jaesik Park</b>')

	if len(author) == 2:
		return author[0] + ' and ' + author[1]
	else:		
		s = ''
		for a in author[:-1]:
			s += (a + ', ')
		s += 'and ' + author[-1]
		return s

def change_html_bold_to_latex_bold(text):
	text = text.replace('<b>', '\\textbf{')
	text = text.replace('</b>', '}')
	return text

def change_emph(text):
	return '\\emph{' + text + '}'

def change_percent(text):
	text = text.replace('%', '\%')
	return text

def remove_asterisks(text):
	text = text.replace('*', '')
	return text

def remove_html_bold(text):
	text = text.replace('<b>', '')
	text = text.replace('</b>', '')
	return text

def remove_special_characters(text):
	text = ''.join(e for e in text if e.isalnum())
	return text

def clear_file(file):
	f = open(file, "w")
	f.close()

def indent_multiline_texts(text, tabs):
	s = text.split('\n')
	n = ''
	for i in s[:-1]:
		n += ("	" * tabs) + i + '\n'
	n += ("	" * tabs) + s[-1]
	return n

def include_file(output_file, include_file):
	f = open(include_file, "r")
	copy = open(output_file, "a")
	for line in f:
		copy.write(line)
	f.close()
	copy.close()