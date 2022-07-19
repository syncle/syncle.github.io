import json
from util import remove_asterisks, remove_html_bold, indent_multiline_texts, remove_special_characters

def authorlist_to_bibtex_style(author):
    s = ''
    for a in author[:-1]:
        a = remove_asterisks(a)
        s += (a + ' and ')
    s += author[-1]
    return s

def gen_nickname(i, year):
    first_author = remove_asterisks(i['author'][0]).split()
    first_author_last_name = first_author[-1]
    first_word_in_title = remove_special_characters(i['title'].split()[0])
    venue = i['venue']
    venue_short = remove_html_bold(venue[venue.find("(")+1:venue.find(")")])
    venue_short = venue_short.replace(' ', '_')
    nickname = first_author_last_name + '_' + first_word_in_title + '_' + venue_short + '_' + year
    return nickname

def get_bibtex_proceedings(i, year):
    bibitem = '@inproceedings{%s,<br>' % gen_nickname(i, year) + \
        '\nTitle={%s},<br>' % i['title'] + \
        '\nAuthor={%s},<br>' % authorlist_to_bibtex_style(i['author']) + \
        '\nBooktitle={Proceedings of the %s},<br>' % remove_html_bold(i['venue']) + \
        '\nYear={%s}<br>' % year + \
        '\n}'
    return bibitem

def get_bibtex_article(i, year):
    bibitem = '@article{%s,<br>' % gen_nickname(i, year) + \
        '\nTitle={%s},<br>' % i['title'] + \
        '\nAuthor={%s},<br>' % authorlist_to_bibtex_style(i['author']) + \
        '\nJournal={%s},<br>' % remove_html_bold(i['venue']) + \
        ('\nVolume={%s},<br>' % i['volume'] if 'volume' in i else '') + \
        ('\nNumber={%s},<br>' % i['number'] if 'number' in i else '') + \
        ('\nPages={%s},<br>' % i['pages'] if 'pages' in i else '') + \
        '\n}'
    return bibitem

def get_bibtex_arxiv(i, year):
    bibitem = '@article{%s,<br>' % gen_nickname(i, year) + \
        '\nTitle={%s},<br>' % i['title'] + \
        '\nAuthor={%s},<br>' % authorlist_to_bibtex_style(i['author']) + \
        '\nJournal={%s},<br>' % remove_html_bold(i['venue']) + \
        '\nYear={%s}<br>' % year + \
        '\n}'
    return bibitem

def get_bibtex_str(i, year):
    if i['type'] == 'conference':
        return get_bibtex_proceedings(i, year)
    elif i['type'] == 'journal':
        return get_bibtex_article(i, year)
    elif i['type'] == 'arxiv':
        return get_bibtex_arxiv(i, year)

def get_collapsed_bibtex_html(i, year):
    nickname = gen_nickname(i, year)
    nickname_button = nickname + "_bibtex_button"
    bibtex = get_bibtex_str(i, year)
    button = '<a class="btn btn-outline-secondary btn-sm" role="button" data-bs-toggle="collapse" data-bs-target="#%s" aria-expanded="false" aria-controls="%s">BibTeX</a>' % (nickname_button, nickname_button)
    button = indent_multiline_texts(button, 4)
    bibtex = indent_multiline_texts(bibtex, 4)
    box = '<div class="collapse" id="%s_bibtex_button">\n' % nickname + \
            '	<div class="card">\n' + \
            '		<div class="card-body">\n' + \
            '			<p class="card-text text-start fw-lighter">\n' + \
            '%s' % bibtex + '\n' + \
            '			</p>\n' + \
            '		</div>\n' + \
            '	</div>\n' + \
            '</div>'
    box = indent_multiline_texts(box, 3)
    return button, box, nickname

def test(data):
    for year in data:
        items_international = []
        for category, items in data[year].items():
            if category == 'papers':
                for i in items:
                    if i['language'] == 'international':
                        items_international.append(i)
        for i in items_international:
            print(get_bibtex_str(i, year))

if __name__ == "__main__":
    with open('../data/record.json') as f:
        data = json.load(f)
    test(data)