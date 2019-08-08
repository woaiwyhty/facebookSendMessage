from urllib import request
from urllib import parse
import util
import uuid
import random
import time
import json
from socket import *
from imageGenerate import imageGenerate
from configparser import ConfigParser
import ssl
from bitly import bitlyCore
class fbFriendsAdder():
    m_imageGenerate = None
    opener = None
    m_bitly = None
    deviceid = ''
    sessionID = ''
    password = ''
    phone = ''
    originPhone = ''
    userid = ''
    token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    authToken = ''
    uploadStrPacket = ''
    latitude = ''
    longitude = ''
    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)[FBAN/FB4A;FBAV/42.0.0.27.114;FBPN/com.facebook.katana;FBLC/en_US;FBBV/14063944;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A5000;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1600,height=900};FB_FW/1;]',
        'X-FB-Connection-Type': 'WIFI',
        'x-fb-net-hni': '',
        'x-fb-sim-hni': '',
        'X-FB-HTTP-Engine': 'Apache',
        'Transfer-Encoding': 'chunked',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive'
    }
    def __init__(self, uploadStrPacket, imageGen, username, password, deviceid = '', autoToken = ''):
        # multiprocessing.Process.__init__(self)
        self.uploadStrPacket = uploadStrPacket
        self.m_imageGenerate = imageGen
        self.phone = username
        self.password = password
        if deviceid == '':
            deviceid = uuid.uuid1().__str__()
        self.authToken = autoToken
        self.deviceid = deviceid
        self.m_bitly = bitlyCore()
        random.seed()

    def waitRandom(self):
        for i in range(1, 2):
            time.sleep(random.random())
    def waitPeriod(self, a, b):
        for i in range(a, b):
            time.sleep(random.random())
    def headerTemplate(self):
        return {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)[FBAN/FB4A;FBAV/42.0.0.27.114;FBPN/com.facebook.katana;FBLC/en_US;FBBV/14063944;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A5000;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1600,height=900};FB_FW/1;]',
            'X-FB-Connection-Type': 'WIFI',
            'x-fb-net-hni': '',
            'x-fb-sim-hni': '',
            'X-FB-HTTP-Engine': 'Apache',
            'Transfer-Encoding': 'chunked',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive'
        }

    def setup(self, ipuser = 'sp06986840', ippass = 'wyhty2627',
                 ipdomain = 'us.smartproxy.com', ipport = '10000'):
        for i in range(0, 3):
            try:
                self.opener = request.build_opener(request.ProxyHandler(
                    {
                        'http': 'http://%s:%s@%s:%s' % (ipuser, ippass, ipdomain, ipport),
                        'https': 'http://%s:%s@%s:%s' % (ipuser, ippass, ipdomain, ipport),
                    }
                ))
                # self.opener = request.build_opener()
                # self.opener = request.build_opener(request.ProxyHandler(
                #     {
                #         'http': 'http://192.168.0.11:8888',
                #         'https': 'http://192.168.0.11:8888',
                #     }
                # ))
                # self.opener = request.build_opener(request.ProxyHandler(
                #     {
                #         'http': 'http://YYVsg2:eg31Ys@168.235.71.168:40609',
                #         'https': 'https://YYVsg2:eg31Ys@168.235.71.168:40609',
                #     }
                # ))
                print('开始测IP')
                page = self.opener.open('http://lumtest.com/myip.json', timeout=5).read().decode('utf-8')
                res = json.loads(page)
                self.latitude = str(res['geo']['latitude'])
                self.longitude = str(res['geo']['longitude'])
                print(page)
                print('开始登录bitly')
                self.m_bitly.login(bitlyUser, bitlyPass)
                print('初始化注册成功')

                break
            except Exception as inst:
                print('IP获取失败, 开始重试')


    def login(self):
        self.sessionID = uuid.uuid1().__str__()
        url = 'https://api.facebook.com/method/logging.clientevent'
        message = '{"time":1562474285756,"app_ver":"42.0.0.27.114","build_num":14063944,"session_id":"{sessionID}","seq":0,"uid":null,"tier":"regular","app_id":"350685531728","device_id":"{deviceID}","carrier":"中国移动","device":"MuMu","os_ver":"6.0.1","conn":"WIFI","sent_time":"1562474295.127","config_checksum":"","config_version":"v2","data":[{"time":"1562474285.756","log_type":"client_event","name":"app_new_install","extra":{"tracking_enabled":true,"process":"com.facebook.katana"},"bg":true},{"time":"1562474291.68","log_type":"client_event","name":"marauder_beacon","module":"marauder","extra":{"impl":"analytics1","tier":"regular","beacon_id":1,"process":"com.facebook.katana"}},{"time":"1562474285.788","log_type":"client_event","name":"navigation","module":"unknown","extra":{"dest_module":"login_screen","click_point":"foreground","dest_module_class":"FacebookLoginActivity","activity_stack_size":1,"process":"com.facebook.katana"}}]}'
        message = message.replace('{sessionID}', self.sessionID).replace('{deviceID}', self.deviceid)
        dataMap = {
            'message' : message,
            'compressed': '0',
            'format': 'json',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'logging.clientevent',
            'fb_api_req_friendly_name': 'sendAnalyticsLog',
            'fb_api_caller_class': 'com.facebook.analytics.service.AnalyticsQueue',
            'access_token': self.token,
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth null'
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()

    def getMachineID(self):
        arr = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ-zyxwvutsrqponmlkjihgfedcba', 24)
        return ''.join(arr)
    def getBatch(self):
        machineID = self.getMachineID()
        batch = '[{"method":"POST","body":"format=json&device_id='+self.deviceid+'&email='+self.phone+'&password='+self.password+'&credentials_type' \
                                                                                 '=password&generate_session_cookies=1&error_detail_type=button_with_disabled&machine_id='+machineID+'&locale=en_US&client_country_code=US&fb_api_req_friendly_name=authenticate","name":"authen' \
                'ticate","omit_response_on_success":false,"relative_url":"method/auth.login"},{"method":"POST","body":"query_params=%7B%220%22%3A84%2C%221%22%3A135%2C%222%22%3A540%7D&method=get&query_id=10153437257771729&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=GetLoggedInUserQuery","name":' \
                '"getLoggedInUser","depends_on":"authenticate","omit_response_on_success":false,"relative_url":"graphql?' \
                'access_token={result=authenticate:$.access_token}"}]'
        return batch

    def OAuth(self):
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % (self.token)
        dataMap = {
            'batch' : self.getBatch(),
            'fb_api_caller_class' : 'com.facebook.katana.server.handler.Fb4aAuthHandler',
            'fb_api_req_friendly_name' : 'authLogin'
        }
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request('https://b-graph.facebook.com/?include_headers=false&locale=en_US&client_country_code=US', headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        page = page.decode('utf-8')
        print(page)
        if page.find('User must verify their account on www.facebook.com') != -1:
            raise Exception('账号需要审核')
        boolRes, self.authToken = util.getAccessToken(page)
        if boolRes == False:
            raise Exception('获取access token失败')
        boolRes, self.userid = util.getUID(page)
        if boolRes == False:
            raise Exception('获取UID失败')

    def getUserID(self):
        url = 'https://b-api.facebook.com/method/bookmarks.get'
        dataMap = {
            'format': 'JSON',
            'one_column': 'true',
            'icon_style': 'caspian',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'bookmarks.get',
            'fb_api_req_friendly_name': 'bookmarkSync',
            'fb_api_caller_class': 'com.facebook.bookmark.client.BookmarkSyncQueue',
        }
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        page = page.decode('utf-8')
        print(page)
        res = json.loads(page)
        if page.find('Error validating access token: The user is enrolled in a blocking') != -1:
            raise Exception('账号需要审核')
        return res[0]['all'][0]['id']

    def getPlaceID(self):
        url = 'https://api.facebook.com/method/fql.query'
        dataMap = {
            'query': "SELECT abbr_name, type, page_fbid FROM geo_region WHERE ((latitude = '%s' AND longitude = '%s') AND type = 'city')" % (self.latitude, self.longitude),
            'format': 'json',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'fql.query',
            'fb_api_req_friendly_name': 'fqlQueryMethod',
            'fb_api_caller_class': 'com.facebook.composer.protocol.ComposerService$1',
        }
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')

        req = request.Request(url, headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read()
        page = page.decode('utf-8')
        print(page)
        res = json.loads(page)
        return res[0]['page_fbid']

    def randomFileName(self):
        arr = random.sample('zyxwvutsrqponmlkjihgfedcba', 15)
        return ''.join(arr)

    def randomMessage(self, message):
        arr = random.sample('zyxwvutsrqponmlkjihgfedcba', 10)
        arr1 = random.sample('zyxwvutsrqponmlkjihgfedcba123456789', 10)
        front = ''.join(arr)
        back = ''.join(arr1)
        return parse.quote(front + message + back, 'utf-8')

    def findTagList(self):
        url = 'https://graph.facebook.com/graphql'
        dataMap = {
            'query_id': '10153621895131729',
            'strip_nulls': 'true',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'FetchChatContextsQuery',
            'fb_api_caller_class': 'com.facebook.contacts.service.DynamicContactDataQueue',
        }
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read().decode('utf-8')
        res = json.loads(page)
        if self.userid in res:
            res = res[self.userid]
            if 'friends' in res:
                res = res['friends']
                if 'nodes' in res:
                    res = res['nodes']
                    return True, res
        return False, page

    def uploadPhoto(self, sessionID, placeID):
        path = self.m_imageGenerate.process_profile()
        url = 'https://graph.facebook.com/me/photos'
        newHeader = self.headerTemplate()
        newHeader['Authorization'] = 'OAuth %s' % self.authToken
        newHeader['Content-Type'] = 'multipart/form-data; boundary=f7wb4i1DGz0AFgbIESoIXozYcljQo1N6m2v6Q3Fk'
        str = self.uploadStrPacket.replace('{sessionID}', sessionID).replace('{placeID}', placeID).replace('{filename}', self.randomFileName())
        packetByte = str.encode(encoding='UTF-8')

        with open(path, "rb") as f:
            imgBytes = f.read()
        self.m_imageGenerate.removeFile(path)
        data = packetByte + imgBytes + '\n--f7wb4i1DGz0AFgbIESoIXozYcljQo1N6m2v6Q3Fk'.encode(encoding='UTF-8')
        req = request.Request(url, headers=newHeader, data=data)  # POST方法
        page = self.opener.open(req, timeout=60).read()
        page = page.decode('utf-8')
        jsonRes = json.loads(page)
        if 'id' not in jsonRes:
            return False, '上传头像失败'
        return True, jsonRes['id']

    def post(self, sessionID, photoID, placeID, message, tags):
        url = 'https://graph.facebook.com/?include_headers=false&decode_body_json=false&streamable_json_response=true&locale=en_US&client_country_code=US'
        tagStr = '[%s]' % ','.join(tags)
        tagStr = parse.quote(tagStr, 'utf-8')
        batch = '[{"method":"POST","body":"published=true&name={message}&place={placeID}&tags={tagStr}&source_type=feed_inline&privacy=%7B%22value%22%3A%22EVERYONE%22%7D&audience_exp=true&qn={sessionID}&composer_session_id={sessionID}&idempotence_token={sessionID}_0-publish&is_explicit_location=false&time_since_original_post=1&connection_class=EXCELLENT&locale=en_US&client_country_code=US&fb_api_req_friendly_name=publish-photo","name":"publish","omit_response_on_success":false,"relative_url":"{photoID}"},{"method":"POST","body":"query_params=%7B%2212%22%3A68%2C%220%22%3A%22{photoID}%22%2C%222%22%3A810%2C%2215%22%3A68%2C%2219%22%3A%222%22%2C%2233%22%3A%22feed%22%2C%2216%22%3A%22false%22%2C%2217%22%3A20%2C%223%22%3A%22image%2Fjpeg%22%2C%2214%22%3A%22image%2Fx-auto%22%2C%2238%22%3A%22contain-fit%22%2C%2236%22%3A1080%2C%2237%22%3A2048%2C%2241%22%3A540%2C%2242%22%3A2048%2C%2239%22%3A122%2C%2240%22%3A2048%2C%2243%22%3A21%2C%2244%22%3A2048%2C%226%22%3A559%2C%225%22%3A1080%2C%2213%22%3A%22true%22%2C%2234%22%3A%22true%22%2C%2235%22%3A%22false%22%2C%2226%22%3A%22true%22%2C%2222%22%3A%22false%22%2C%2223%22%3A3%2C%2224%22%3A%22true%22%2C%2216%22%3A%22false%22%2C%2217%22%3A20%7D&method=get&query_id=10153948981866729&strip_nulls=true&strip_defaults=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=StaticGraphQlCreationStoryQuery","name":"fetchCreationStory","depends_on":"publish","omit_response_on_success":false,"relative_url":"graphql"}]'
        batch = batch.replace('{placeID}', placeID).replace('{photoID}', photoID).replace('{sessionID}', sessionID)
        batch = batch.replace('{tagStr}', tagStr).replace('{message}', self.randomMessage(message))
        dataMap = {
            'batch': batch,
            'fb_api_caller_class': 'com.facebook.photos.upload.protocol.PhotoPublisher',
            'fb_api_req_friendly_name': 'single_photo_publish',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=60).read().decode('utf-8')
        res = json.loads(page)
        print(res)

    def findRequestList(self):
        url = 'https://graph.facebook.com/graphql'
        dataMap = {
            'query_params': '{"1":"10","2":"image/x-auto","3":"108"}',
            'method': 'get',
            'query_id': '10153086649741729',
            'strip_nulls': 'true',
            'strip_defaults': 'true',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'FriendRequestQuery',
            'fb_api_caller_class': 'com.facebook.friending.jewel.FriendRequestsFragment',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=15).read().decode('utf-8')
        res = json.loads(page)
        if 'viewer' in res:
            res = res['viewer']
            if 'friending_possibilities' in res:
                res = res['friending_possibilities']
                if 'edges' in res:
                    res = res['edges']
                    return True, res
                else:
                    return True, []
        return False, page

    def acceptRequests(self, friends):
        url = 'https://graph.facebook.com/graphql'
        for friend in friends:
            print('开始同意下一个好友申请')
            mutualID = uuid.uuid1().__str__()
            dataMap = {
                'query_params': '{"input":{"source":"m_jewel","friend_requester_id":"%s","client_mutation_id":"%s","actor_id":"%s"}}' % (friend['node']['id'], mutualID, self.userid),
                'method': 'post',
                'query_id': '10153545452586729',
                'strip_nulls': 'true',
                'strip_defaults': 'true',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'FriendRequestAcceptCoreMutation',
                'fb_api_caller_class': 'com.facebook.friends.protocol.FriendMutationsModels$FriendRequestAcceptCoreMutationFieldsModel',
            }
            newHeaders = self.headerTemplate()
            newHeaders['Authorization'] = 'OAuth %s' % self.authToken
            data = parse.urlencode(dataMap).encode('utf-8')
            req = request.Request(url, headers=newHeaders, data=data)  # POST方法
            page = self.opener.open(req, timeout=15).read().decode('utf-8')
            print(page)
            self.waitRandom()

    def postInTimelime(self, target, photoID, sessionID, message):
        url = 'https://graph.facebook.com/?include_headers=false&decode_body_json=false&streamable_json_response=true&locale=en_US&client_country_code=US'
        batch = '[{"method":"POST","body":"published=1&target={friendID}&qn={sessionID}&composer_session_id={sessionID}&name={message}&idempotence_token={sessionID}_photo_0&is_explicit_location=false&time_since_original_post=2&batch_size=1&audience_exp=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=attachPhoto","name":"photo_0","omit_response_on_success":false,"relative_url":"{photoID}"},{"method":"POST","body":"query_params=%7B%2212%22%3A68%2C%220%22%3A%22{photoID}%22%2C%222%22%3A810%2C%2215%22%3A68%2C%2219%22%3A%222%22%2C%2233%22%3A%22feed%22%2C%2216%22%3A%22false%22%2C%2217%22%3A20%2C%223%22%3A%22image%2Fjpeg%22%2C%2214%22%3A%22image%2Fx-auto%22%2C%2238%22%3A%22contain-fit%22%2C%2236%22%3A1080%2C%2237%22%3A2048%2C%2241%22%3A540%2C%2242%22%3A2048%2C%2239%22%3A122%2C%2240%22%3A2048%2C%2243%22%3A21%2C%2244%22%3A2048%2C%226%22%3A559%2C%225%22%3A1080%2C%2213%22%3A%22true%22%2C%2234%22%3A%22true%22%2C%2235%22%3A%22false%22%2C%2226%22%3A%22true%22%2C%2222%22%3A%22false%22%2C%2223%22%3A3%2C%2224%22%3A%22true%22%2C%2216%22%3A%22false%22%2C%2217%22%3A20%7D&method=get&query_id=10153948981866729&strip_nulls=true&strip_defaults=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=StaticGraphQlCreationStoryQuery","name":"fetch","depends_on":"photo_0","omit_response_on_success":false,"relative_url":"graphql"}]'
        batch = batch.replace('{photoID}', photoID).replace('{sessionID}', sessionID)
        batch = batch.replace('{message}', self.randomMessage(message)).replace('{friendID}', target)
        dataMap = {
            'batch': batch,
            'fb_api_caller_class': 'com.facebook.photos.upload.protocol.PhotoPublisher',
            'fb_api_req_friendly_name': 'multi_photo_publish_target',
        }
        newHeaders = self.headerTemplate()
        newHeaders['Authorization'] = 'OAuth %s' % self.authToken
        data = parse.urlencode(dataMap).encode('utf-8')
        req = request.Request(url, headers=newHeaders, data=data)  # POST方法
        page = self.opener.open(req, timeout=60).read().decode('utf-8')
        res = json.loads(page)
        print(res)

    def generateBitly(self):
        arr = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba1234567890', 10)
        return ''.join(arr)
    def runMode1(self):
        try:
            self.setup(ipuser, ippass, ipdomain, ipport)
            if len(self.authToken) < 10:
                self.login()
                self.OAuth()
            else:
                print('已经有令牌, 直接开始获取用户ID')
                m_friend.userid = self.getUserID()
                print(m_friend.userid)
            print('开始通过好友请求...')
            boolRes, friends = self.findRequestList()
            if boolRes == False:
                raise Exception('读取好友请求失败')
            else:
                self.acceptRequests(friends)
                print('通过好友请求成功')
            for i in range(0, len(adsTextList)):
                print('开始获取位置ID')
                placeID = self.getPlaceID()
                print('开始上传图片')
                sessionID = uuid.uuid1().__str__()
                self.waitRandom()
                boolRes, photoID = self.uploadPhoto(sessionID, placeID)
                if boolRes == False:
                    print('上传图片失败')
                    continue
                self.waitPeriod(2, 4)
                print('开始获取标记好友列表')
                boolRes, tagList = self.findTagList()
                if boolRes == False:
                    print('获取标记好友列表失败')
                    continue
                kk = random.randint(minimum_tags, maximum_tags)
                if len(tagList) < kk:
                    kk = len(tagList)
                chosen = random.choices(tagList, k = kk)
                idChosen = []
                for j in chosen:
                    idChosen.append(j['id'])
                print('正在发帖...')
                bitlyID = self.generateBitly()
                self.post(sessionID, photoID, placeID, adsTextList[i] + '\r\n' + 'http://bit.ly/' + bitlyID + '\r\n', idChosen)
                print('发帖成功, 随机延迟后继续...')
                self.waitPeriod(5, 10)
                print('开始申请bitly链接  http://bit.ly/%s' % bitlyID)
                print(self.m_bitly.createShortURL(adsLinkList[i], bitlyID))
            return '操作成功'
        except Exception as inst:
            print(inst.args)
            if len(inst.args) > 0 and inst.args[0] == '账号需要审核':
                return '账号需要审核'
            return '操作失败'

    def runMode2(self):
        try:
            self.setup(ipuser, ippass, ipdomain, ipport)
            if len(self.authToken) < 10:
                self.login()
                self.OAuth()
            else:
                print('已经有令牌, 直接开始获取用户ID')
                m_friend.userid = self.getUserID()
                print(m_friend.userid)
            print('开始通过好友请求...')
            boolRes, friends = self.findRequestList()
            if boolRes == False:
                raise Exception('读取好友请求失败')
            else:
                self.acceptRequests(friends)
                print('通过好友请求成功')
            print('开始获取好友列表')
            boolRes, tagList = self.findTagList()
            if boolRes == False:
                raise Exception('获取好友列表失败')
            chosen = random.choices(tagList, k=post_num)
            idChosen = []
            for j in chosen:
                idChosen.append(j['id'])
            for i in range(0, len(idChosen)):
                print('开始获取位置ID')
                placeID = self.getPlaceID()
                print('开始上传图片')
                sessionID = uuid.uuid1().__str__()
                self.waitRandom()
                boolRes, photoID = self.uploadPhoto(sessionID, placeID)
                if boolRes == False:
                    print('上传图片失败')
                    continue
                self.waitPeriod(2, 4)
                print('正在发帖...')
                bitlyID = self.generateBitly()
                self.postInTimelime(idChosen[i], photoID, sessionID, adsTextList[i] + '\r\n' + 'http://bit.ly/' + bitlyID + '\r\n')
                print('发帖成功, 随机延迟后继续...')
                self.waitPeriod(5, 10)
                print('开始申请bitly链接  http://bit.ly/%s' % bitlyID)
                print(self.m_bitly.createShortURL(adsLinkList[i], bitlyID))
            return '操作成功'
        except Exception as inst:
            print(inst.args)
            if len(inst.args) > 0 and inst.args[0] == '账号需要审核':
                return '账号需要审核'
            return '操作失败'

if __name__ == '__main__':

    # m_imageGenerate = imageGenerate('profilephoto')
    # with open('./base/uploadPhoto', "r") as f:  # 设置文件对象
    #     uploadStrPacket = f.read()  # 可以是随便对文件的操作
    # m_friend = fbFriendsAdder(uploadStrPacket, m_imageGenerate, 'x.love50@yahoo.com', 'qaz123654.')
    #
    # m_friend.setup()
    # m_friend.login()
    # m_friend.OAuth()
    # placeID = m_friend.getPlaceID()
    # print(placeID)
    # boolRes, friendsList = m_friend.findTagList()
    # chosen = random.choices(friendsList, k = 3)
    # idChosen = []
    # for i in chosen:
    #     idChosen.append(i['id'])
    #
    # sessionID = uuid.uuid1().__str__()
    # boolRes, friends = m_friend.findRequestList()
    # # m_friend.acceptRequests(friends)
    #
    # a, b = m_friend.uploadPhoto(sessionID, placeID)
    # print(a)
    # print(b)
    # if a == True:
    #     m_friend.postInTimelime(idChosen[0], b, sessionID, 'こんにちは')
    # if a == True:
    #     m_friend.post(sessionID, b, placeID, 'こんにちは', idChosen)
    # word = m_friend.searchWords()
    # a, b = m_friend.searchMainPage(word['name'])
    # a, b = m_friend.openMainPage(word['id'])
    # print(a)
    # print(b)
    # tracking = b[0]['node']['tracking']
    # shareID = b[0]['node']['shareable']['id']
    # storyID= b[0]['node']['legacy_api_story_id']
    # print(tracking)
    # print(shareID)
    # print(storyID)
    # # print(m_friend.like(storyID, tracking))
    #
    # print(m_friend.share(shareID, tracking))
    # exit()

    # print('开始')
    # time.sleep(1)
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        cp = ConfigParser()
        cp.read("peizhi.cfg", encoding='utf-8')
        ipuser = cp.get('ip', 'ipUser')
        ippass = cp.get('ip', 'ipPass')
        ipdomain = cp.get('ip', 'ipDomain')
        ipport = cp.get('ip', 'ipPort')
        serverIP = cp.get('others', 'serverIP')
        minimum_tags = int(cp.get('others', 'minimum_tags'))
        maximum_tags = int(cp.get('others', 'maximum_tags'))
        mode = cp.get('others', 'mode')
        post_num = int(cp.get('others', 'post_num'))
        with open('./base/uploadPhoto', "r") as f:  # 设置文件对象
            uploadStrPacket = f.read()  # 可以是随便对文件的操作
        time.sleep(1)
        m_imageGenerate = imageGenerate('profilephoto')
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        time.sleep(1)
        print('开始连接')
        tcp_client_socket.connect((serverIP, 19760))
    except Exception as inst:
        print("线程初始化失败, 请重新开启")
        exit()

    BUFSIZE = 65535
    print('连接加好友服务器成功, 开始等待账号')
    while True:
        tcp_client_socket.send(b'RequestAccount|')
        data = tcp_client_socket.recv(BUFSIZE).decode('gbk')
        if not data:
            print('与服务器断开连接')
            break
        # print('得到账号 %s' % data)
        arr = data.split('\t')
        print(arr)
        adsTextList = arr[6].split('|||')
        adsLinkList = arr[7].split('|||')
        bitlyUser = arr[4]
        bitlyPass = arr[5]
        auth = arr[8]
        m_friend = fbFriendsAdder(uploadStrPacket, m_imageGenerate, arr[1], arr[2], arr[3], auth)
        print(auth)
        if mode  == '1':
            res = m_friend.runMode1()
        else:
            res = m_friend.runMode2()

        sendData = 'FinishAccount|%s|%s|%s' % (arr[0], res, m_friend.authToken)
        tcp_client_socket.send(sendData.encode(encoding='gbk'))
        print('操作完成, 继续等待新的账号')
        time.sleep(2)

    tcp_client_socket.close()
