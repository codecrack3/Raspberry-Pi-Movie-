import requests
import json
import random
def checkurl(link):
	if 'tap' in link:
		playid = link.split('.')[1].split('-')[-1]
		epid = link.split('.')[1].split('-')[-2]
	else:
		playid = link.split('.')[1].split('-')[-1]
		epid = '1';
	return playid,epid

def getlink(playid,epid):
	user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9']
	rawBody = "Connection: close\r\n\r\n\r\n"
	headers = {"User-Agent":"%s"  % str(random.choice(user_agents)),"Accept-Language":"en-US,en;q=0.8,vi;q=0.6","Accept":"application/json, text/javascript, */*; q=0.01",'referer': 'http://hdonline.vn'} 
	response = requests.get("http://api.hdonline.vn/v2/episode/getlink?ep=%s&filmid=%s&token=hdoplayerapi" %(epid,playid) , data=rawBody, headers=headers)
	
	return json.loads(response.text)

url = raw_input('Link ? ')
s = checkurl(url)
print s[0],s[1]
print getlink(s[0],s[1])
print getlink(s[0],s[1])['result'][0]['link']
# print getlink(s[0],s[1])['subtitle'][-1]['file']
# #print getlink(s[0],s[1])['level'][-1]['file']
# print getlink(s[0],s[1])['file']
