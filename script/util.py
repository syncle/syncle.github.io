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


def authorlist_to_text(author):
	# adding special action for my name?
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

def change_bold(text):
	# adding special action for my name?
	# import ipdb; ipdb.set_trace()
	text = text.replace('<b>', '\\textbf{')
	text = text.replace('</b>', '}')
	return text

def change_emph(text):
	return '\\emph{' + text + '}'

def change_percent(text):
	text = text.replace('%', '\%')
	return text

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