import pypandoc
from bs4 import BeautifulSoup
CH = 'h2'

class book:
    html_book = None
    def __init__(self, name):
        self.filename = name
        self.read_from_epub()
        self.open_html_book()

    def read_from_epub(self):
        new_filename = self.filename[:-4] + 'html'
        pypandoc.convert_file(self.filename, 'html', outputfile= new_filename)
        self.filename = new_filename

    def open_html_book(self):
        with open(self.filename, encoding='UTF-8') as fp:
            self.html_book = BeautifulSoup(fp, 'html.parser')

    def get_chapt(self, num, part = 0):
        headers = self.html_book.find_all(CH)
        chapter = [headers[num-1]]
        if num == len(headers):
            chapter += chapter[0].find_all_next()
        else:
            el = chapter[0]
            while el is not headers[num]:
                el = el.find_next()
                if el is not headers[num]:
                    chapter.append(el)
        chapter = [el.get_text() for el in chapter]
        length = 1
        res = []
        for el in chapter:
            if length + len(el) < 4000 * (part + 1) and length > 4000 * part:
                res.append(el)
                length +=len(el)
        return '\n'.join([el for el in res])

