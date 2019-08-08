import json
import re
def logMessage(message):
    print(message)



def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr, startIndex + 1)
  return content[startIndex:endIndex]
def getAccessToken(message):
    # pattern = re.compile('access_token\\":\\"(.*?)\\"')
    # a = pattern.search(message)
    # b = a.groups()
    # if len(b) > 0:
    #     return True, b[0]
    # return False, ''
    res = GetMiddleStr(message, 'access_token\\":\\"', '\\",')
    if len(res) > 0:
        return True, res
    return False, ''

def getUID(message):
    res = GetMiddleStr(message, 'uid\\":', ',')
    if len(res) > 0:
        return True, res
    return False, ''
# header = {
#     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)[FBAN/FB4A;FBAV/42.0.0.27.114;FBPN/com.facebook.katana;FBLC/en_US;FBBV/14063944;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A5000;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1600,height=900};FB_FW/1;]',
#     'X-FB-Connection-Type': 'WIFI',
#     'x-fb-net-hni': '',
#     'x-fb-sim-hni': '',
#     'X-FB-HTTP-Engine': 'Apache',
#     'Transfer-Encoding': 'chunked',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Connection': 'Keep-Alive'
# }
# newheader = header
# newheader['asdasfaa'] = 'agsafasfsafa'
# print(header)
# print(newheader)
# print(json.loads('[{"code":200,"body":"{"error_code":405,"error_msg":"User must verify their account on www.facebook.com (405)","error_data":"{"url":"https://www.facebook.com/checkpoint/start/?ip=160.255.118.112&cookie=u00257Bu002522uu002522u00253A100039356881416u00252Cu002522tu002522u00253A1562831642u00252Cu002522stepu002522u00253A0u00252Cu002522nu002522u00253Au002522u00252BXdS1B6GTksu00253Du002522u00252Cu002522instu002522u00253A100504604604769u00252Cu002522fu002522u00253A1501092823525282u00252Cu002522stu002522u00253Au002522pu002522u00252Cu002522aidu002522u00253Anullu00252Cu002522cau002522u00253Anullu00252Cu002522lau002522u00253Au002522u002522u00252Cu002522tau002522u00253Au0025221562831645.ch.su00253Apw.tDBFAiAZ5hZ7Z1UlpiLdQ49qRshIlHrLVpkiyEsIqCyyr_lO9wIhAP4L7IszYb7CrAJE8p-MhrczeDJE0gd6Q4DF0SOuBB3Zu002522u00252Cu002522satu002522u00253Anullu00252Cu002522su002522u00253Au002522AWWpeR5WH6Q5QHmfu002522u00252Cu002522csu002522u00253Au00255Bu00255Du00257D&next=fbu00253Au00252Fu00252F&hash=AWX181KLlE3EMKuU","flow_id":1501092823525282,"uid":100039356881416,"show_native_checkpoints":false,"start_internal_webview_from_url":true,"positive_button_string":"Get Started","error_title":"Confirm Your Identity","error_message":"To log into your Facebook account, you need to first confirm your identity."}","request_args":[{"key":"method","value":"auth_login"},{"key":"format","value":"json"},{"key":"version","value":""},{"key":"_fb_batch_child_request","value":"1"},{"key":"_fb_batch_expires","value":"1562831662"},{"key":"_fb_batch_sig","value":"Afi_AYfOrmme8tx6"},{"key":"device_id","value":"0733e708-a3b1-11e9-aa07-204747765919"},{"key":"email","value":"8618324685429"},{"key":"password","value":"--sanitized--"},{"key":"credentials_type","value":"password"},{"key":"generate_session_cookies","value":"1"},{"key":"error_detail_type","value":"button_with_disabled"},{"key":"machine_id","value":"JsCLHmnN-rckTvExUzigVadw"},{"key":"locale","value":"en_US"},{"key":"client_country_code","value":"US"},{"key":"fb_api_req_friendly_name","value":"authenticate"},{"key":"_fb_url","value":"method/auth.login"},{"key":"fb_api_caller_class","value":"com.facebook.katana.server.handler.Fb4aAuthHandler"},{"key":"access_token","value":"--sanitized--"},{"key":"_fb_profilable_request_id","value":"3211794656"}]}"},null]'))
# print(json.loads('[{"code":200,"body":"{\"session_key\":\"5.BegUYqlehZdw4w.1562054052.32-100038706318672\",\"uid\":100038706318672,\"secret\":\"15ef9af49d6eb5b3597373c1477f38b0\",\"access_token\":\"EAAAAUaZA8jlABAHqQtCJlAwO4RTGJ2OMGMuCJdZBtz2WlW4yaGdzEpNZBwEa1NFPc5QooBeVj4LkJsas6kwFLNeeAdh3nwouy4zYqZBFW5XuZBFK5IMApZBzswVXyiM9uCZAGgpG8pKvhZCnq4FFYXsHeCbG1Qbt2dAA7ZBXkobvnk07msumtFH53zeW1fcH0RQsZD\",\"machine_id\":\"pA0bXUWdLddpb5MDb484fJtg\",\"session_cookies\":[{\"name\":\"c_user\",\"value\":\"100038706318672\",\"expires\":\"Wed, 01 Jul 2020 07:54:12 GMT\",\"expires_timestamp\":1593590052,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true},{\"name\":\"xs\",\"value\":\"32:BegUYqlehZdw4w:2:1562054052:-1:-1\",\"expires\":\"Wed, 01 Jul 2020 07:54:12 GMT\",\"expires_timestamp\":1593590052,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true,\"httponly\":true},{\"name\":\"fr\",\"value\":\"3Jae3XFaqASPsUMQX.AWXeDtQIfjIM1Xe-gz5oAe6y3wE.BdGw2k..AAA.0.0.BdGw2k.AWWS2x2q\",\"expires\":\"Wed, 01 Jul 2020 07:54:10 GMT\",\"expires_timestamp\":1593590050,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true,\"httponly\":true},{\"name\":\"datr\",\"value\":\"pA0bXUWdLddpb5MDb484fJtg\",\"expires\":\"Thu, 01 Jul 2021 07:54:12 GMT\",\"expires_timestamp\":1625126052,\"domain\":\".facebook.com\",\"path\":\"\\\/\",\"secure\":true,\"httponly\":true}],\"confirmed\":false,\"identifier\":\" 8618714774628\",\"user_storage_key\":\"ef027d8de3fcc0d2e3c6e21e6f395a8396f03225a6d8a5abe0b67fbade7776c4\"}"},{"code":200,"body":"{\"viewer\":{\"actor\":{\"__type__\":{\"name\":\"User\"},\"id\":\"100038706318672\",\"name\":\"Julieta Chandler\",\"structured_name\":{\"text\":\"Julieta Chandler\",\"parts\":[{\"part\":\"first\",\"offset\":0,\"length\":7},{\"part\":\"last\",\"offset\":8,\"length\":8}]},\"is_mobile_pushable\":false,\"all_phones\":[],\"email_addresses\":[],\"squareProfilePicSmall\":{\"uri\":\"https:\\\/\\\/scontent-atl3-1.xx.fbcdn.net\\\/v\\\/t1.0-1\\\/c25.0.86.86a\\\/p86x86\\\/1379841_10150004552801901_469209496895221757_n.jpg?_nc_cat=1&_nc_oc=AQnbxAxNB8gVUBEv_0_FJxuYh17LqK7wyrXngzmHGyetCGSngX3o-_JZMaxr_dYU4WU&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent-atl3-1.xx&oh=d4361f3fd6557ee70a5f912c7a368cce&oe=5D82439C\",\"width\":86,\"height\":86},\"squareProfilePicBig\":{\"uri\":\"https:\\\/\\\/scontent-atl3-1.xx.fbcdn.net\\\/v\\\/t1.0-1\\\/c43.0.148.148a\\\/p148x148\\\/1379841_10150004552801901_469209496895221757_n.jpg?_nc_cat=1&_nc_oc=AQnbxAxNB8gVUBEv_0_FJxuYh17LqK7wyrXngzmHGyetCGSngX3o-_JZMaxr_dYU4WU&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent-atl3-1.xx&oh=05eab340166ffef6125ea61fb2e197a3&oe=5DBA98D8\",\"width\":148,\"height\":148},\"squareProfilePicHuge\":{\"uri\":\"https:\\\/\\\/scontent-atl3-1.xx.fbcdn.net\\\/v\\\/t31.0-1\\\/c212.0.720.720a\\\/p720x720\\\/1402926_10150004552801901_469209496895221757_o.jpg?_nc_cat=1&_nc_oc=AQnbxAxNB8gVUBEv_0_FJxuYh17LqK7wyrXngzmHGyetCGSngX3o-_JZMaxr_dYU4WU&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent-atl3-1.xx&oh=69334a00c0f376b604b2c6e3fa88dd0c&oe=5DC4AED6\",\"width\":720,\"height\":720},\"profile_picture_is_silhouette\":true,\"is_work_user\":false,\"is_minor\":false,\"is_partial\":false},\"is_fb_employee\":false}}"}]'))