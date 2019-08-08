from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import http.cookiejar
import util
import json
class bitlyCore:
    __opener = None
    __cj = None
    __group = ''
    __xsrf = ''
    def __init__(self):
        self.__cj = http.cookiejar.CookieJar()
        self.__opener = request.build_opener(request.HTTPCookieProcessor(self.__cj))
    def headerTemplate(self):
        return {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
    def login(self, username, password):
        url = 'https://bitly.com/a/sign_in'
        req = request.Request(url, headers=self.headerTemplate())
        page = self.__opener.open(req, timeout=15).read().decode('utf-8')
        soup = BeautifulSoup(page, features="html.parser")
        page = soup.prettify()
        xsrf = soup.find('input', {'name': '_xsrf'}).attrs['value']
        print(xsrf)
        # dataMap = {
        #     'username': username,
        #     'password': password,
        #     'rd': '/',
        #     '_xsrf': xsrf,
        #     'verificaton': 'true',
        # }
        # headers = self.headerTemplate()
        #
        # data = parse.urlencode(dataMap).encode('utf-8')
        # req = request.Request(url, headers=self.headerTemplate(), data=data)
        # page = self.__opener.open(req, timeout=15).read().decode('utf-8')
        dataMap = {
            'username': username,
            'password': password,
            'rd': '/',
            '_xsrf': xsrf,
        }
        self.__xsrf = xsrf
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, data=data)
        page = self.__opener.open(req, timeout=15).read().decode('utf-8')
        self.__group = util.GetMiddleStr(page, 'groups: ["', '"]')
        print(self.__group)

    def createShortURL(self, longURL, shortURL):
        url = 'https://app.bitly.com/proxy/v3/user/link_save'
        dataMap = {
            'longUrl': longURL,
            'domain': 'bit.ly',
        }
        headers = self.headerTemplate()
        headers['origin'] = 'https://app.bitly.com'
        headers['x-xsrftoken'] = self.__xsrf
        headers['x-bitly-brand-guid'] = self.__group
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, data=data, headers=headers)
        page = self.__opener.open(req, timeout=15).read().decode('utf-8')
        res = json.loads(page)

        if res['status_code'] == 304 or res['status_code'] == 200:
            myLink = res['data']['link_save']['user_hash']
        else:
            return '失败'


        url = 'https://app.bitly.com/proxy/private/keyword_api_router'
        dataMap = {
            'domain': 'bit.ly',
            'keyword': shortURL,
            'link': 'http://bit.ly/%s' % myLink,
            'overwrite': 'false',

        }
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, data=data, headers=headers)
        page = self.__opener.open(req, timeout=15).read().decode('utf-8')
        print(page)
        res = json.loads(page)
        if res['status_code'] == 200:
            return res['data']['keyword_link']
        else:
            return res['status_txt']

m_bitly = bitlyCore()
m_bitly.login('woaiwyhty@gmail.com', 'wyhty2627')
print(m_bitly.createShortURL('http://www.baidu.com', '2GFKUJBW12534A'))