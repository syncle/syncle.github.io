import json
from util import authorlist_to_text
from gen_button import get_button_str_all

def gen_bibtex_style_author_list(i):
    author_list = ''
    return author_list

def gen_nickname(i):
    nickname = ''
    return nickname

# @inproceedings{arandjelovic2013vlad,
#   Title={All about VLAD},
#   Author={Arandjelovic, Relja and Andrew Zisserman},
#   Booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
#   Year={2013}
# }
def get_bibtex_proceedings(i):
    import ipdb; ipdb.set_trace()
    bibitem = ''
    bibitem = '@inproceedings{%s,' % gen_nickname(i) + \
        '   Title={%s},' % i['title'] + \
        '   Author={%s},' % gen_bibtex_style_author_list(i['author']) + \
        '   Booktitle={%s},' % i['venue'] + \
        '   Year={%s}' % i['year'] + \
        '}'
    return bibitem

# @article{maddern2017RobotCar,
#   Title = {{1 Year, 1000km: The Oxford RobotCar Dataset}},
#   Author = {Will Maddern and Geoff Pascoe and Chris Linegar and Paul Newman},
#   Journal = {The International Journal of Robotics Research (IJRR)},
#   Volume = {36},
#   Number = {1},
#   Pages = {3-15},
#   Year = {2017},
# }
def get_bibtex_article(i):
    bibitem = ''
    bibitem = '@article{%s,' % gen_nickname(i) + \
        '   Title={%s},' % i['title'] + \
        '   Author={%s},' % gen_bibtex_style_author_list(i['author']) + \
        '   Journal={%s},' % i['venue'] + \
        '   Volume={%s},' % i['volume'] + \
        '   Number={%s},' % i['number'] + \
        '   Pages={%s},' % i['pages'] + \
        '   Year={%s}' % i['year'] + \
        '}'
    return bibitem

def get_bibtex_str(i):
    if i['type'] == 'conference':
        return get_bibtex_proceedings(i)
    elif i['type'] == 'journal':
        return get_bibtex_article(i)
    else:
        assert 'Wrong paper types'


def test(data):
    for idx, year in enumerate(data):
        # list up international
        items_international = []
        for category, items in data[year].items():
            if category == 'papers':
                for i in items:
                    if i['type'] == 'international':
                        items_international.append(i)
        # import ipdb; ipdb.set_trace()
        for i in items_international:
            print(i)
            print(get_bibtex_str(i))

if __name__ == "__main__":
    with open('../data/record.json') as f:
        data = json.load(f)
    
    test(data)