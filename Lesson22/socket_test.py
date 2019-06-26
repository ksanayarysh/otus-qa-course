from Lesson22.myhtml_parser import GatherLinks
from Lesson22.myrequests import MyRequests


def test_socket(request, header):
    d = MyRequests(request)
    print(d.headers())
    print(d.get_status_code())
    assert d.get_status_code() == 200
    if header:
        try:
            print(d.headers()[header])
        except KeyError:
            print("No such a key")
    print(d.text())


def test_html_parse(request):
    data = MyRequests(request)
    gather = GatherLinks()
    gather.feed(data.text())
    if request.config.getoption("--links"):
        for link in gather.links:
            print(link)

    if request.config.getoption("--imgs"):
        for img in gather.img:
            print(img)

    if request.config.getoption("--tags"):
        frequency_analysis = dict((i, gather.tags.count(i)) for i in gather.tags)
        sorted_frequency_analysis = sorted(frequency_analysis.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_frequency_analysis:
            print(item)

    if request.config.getoption("--maxtag"):
        frequency_analysis = dict((i, gather.tags.count(i)) for i in gather.tags)
        sorted_frequency_analysis = sorted(frequency_analysis.items(), key=lambda x: x[1], reverse=True)
        print("Most frequent tag: ", sorted_frequency_analysis[0])
