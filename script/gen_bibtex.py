import json
from util import remove_asterisks, remove_html_bold

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
    venue = i['venue']
    venue_short = remove_html_bold(venue[venue.find("(")+1:venue.find(")")])
    venue_short = venue_short.replace(' ', '_')
    nickname = first_author_last_name + '_' + venue_short + '_' + year
    return nickname

def get_bibtex_proceedings(i, year):
    bibitem = '@inproceedings{%s,' % gen_nickname(i, year) + \
        '\n   Title={%s},' % i['title'] + \
        '\n   Author={%s},' % authorlist_to_bibtex_style(i['author']) + \
        '\n   Booktitle={Proceedings of the %s},' % remove_html_bold(i['venue']) + \
        '\n   Year={%s}' % year + \
        '\n}\n'
    print(bibitem)
    return bibitem

def get_bibtex_article(i, year):
    bibitem = '@article{%s,' % gen_nickname(i, year) + \
        '\n   Title={%s},' % i['title'] + \
        '\n   Author={%s},' % authorlist_to_bibtex_style(i['author']) + \
        '\n   Journal={%s},' % remove_html_bold(i['venue']) + \
        ('\n   Volume={%s},' % i['volume'] if 'volume' in i else '') + \
        ('\n   Number={%s},' % i['number'] if 'number' in i else '') + \
        ('\n   Pages={%s},' % i['pages'] if 'pages' in i else '') + \
        '\n}\n'
    print(bibitem)
    return bibitem

def get_bibtex_str(i, year):
    if i['type'] == 'conference':
        return get_bibtex_proceedings(i, year)
    elif i['type'] == 'journal':
        return get_bibtex_article(i, year)
    else:
        assert 'Wrong paper types'


def test(data):
    for year in data:
        items_international = []
        for category, items in data[year].items():
            if category == 'papers':
                for i in items:
                    if i['language'] == 'international':
                        items_international.append(i)
        for i in items_international:
            get_bibtex_str(i, year)

if __name__ == "__main__":
    with open('../data/record.json') as f:
        data = json.load(f)
    # todo: producing txt files?
    test(data)