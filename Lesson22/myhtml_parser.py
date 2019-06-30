from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Encountered a start tag:", tag)
#
#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)
#
#     def handle_data(self, data):
#         print("Encountered some data  :", data)
#
# parser = MyHTMLParser()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')



class GatherLinks(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.img = []
        self.tags = []
        self.full_tags = []

    def handle_starttag(self, tag, attrs):
        # for name, value in attrs:
        self.full_tags.append(tag + str(attrs))
        self.tags.append(tag)

        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    self.img.append(value)


