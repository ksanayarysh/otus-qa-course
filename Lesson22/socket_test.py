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
