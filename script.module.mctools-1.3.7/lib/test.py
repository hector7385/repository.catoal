# coding: utf-8
class Response:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code


class Browser:
    headers = {}
    cookies = {}
    def __init__(self):
        self.headers['User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    def get(self, url='', cookies={}):
        import httplib2
        from urllib import urlencode
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        resp, content = h.request(url, "GET", headers=self.headers, body=urlencode(cookies))
        self.headers['Cookie'] = resp['set-cookie']
        return Response(content, int(resp['status']))

    def post(self, url='', data={}, cookies={}):
        from urllib import urlencode
        import httplib2
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        resp, content = h.request(url,  "POST", urlencode(data), headers=self.headers, body=urlencode(cookies))
        self.headers['Cookie'] = resp['set-cookie']
        return Response(content, int(resp['status']))


browser = Browser()
response = browser.get("https://yts.ag")

print response.status_code
print browser.headers
