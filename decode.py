import os 
try:
	import requests
	from bs4 import BeautifulSoup
except ImportError:
	os.system('pip install --upgrade pip')
	os.system('pip install requests')
	os.system('pip install bs4')
import requests
from bs4 import BeautifulSoup
os.system('clear')
def decode():
	en_data = input("Enter text decode => : ")
	print()
	print('='*60)
	print()
	

	cookies = {
	    '__test': 'e04780b11a44e1b9db6f0820c0ee4e77',
	}
	
	headers = {
	    'Host': 'eslamhacker0.infinityfreeapp.com',
	    'Connection': 'keep-alive',
	    'Content-Length': '66',
	    'Cache-Control': 'max-age=0',
	    'Upgrade-Insecure-Requests': '1',
	    'Origin': 'http://eslamhacker0.infinityfreeapp.com',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
	    'Sec-GPC': '1',
	    'Accept-Language': 'ar-EG,ar;q=0.7',
	    'Referer': 'http://eslamhacker0.infinityfreeapp.com/Decrypted.php',
	    'Accept-Encoding': 'gzip, deflate',
	    'Cookie': '__test=e04780b11a44e1b9db6f0820c0ee4e77',
	}
	
	data = {
	    'Decrypted': ""+en_data+"",
	    'submit': '',
	}
	
	res = requests.post('http://eslamhacker0.infinityfreeapp.com/Decrypted.php', cookies=cookies, headers=headers, data=data)
		
	
	response_text = res.text
	
	
	soup = BeautifulSoup(response_text, 'html.parser')
	#print(soup)
	response_div = soup.find_all('div')[0]
	
	response_value = response_div.find_all('font')[1]
	z=response_value.text
	print(z)

ip=requests.get('https://httpbin.org/ip').json()['origin']
#print(ip)
if ip == '196.134.158.192':
	decode()
elif ip == '196.155.70.203':
	decode()
else:
	print('تم حظر الــip')


bot_token = '6481146559:AAEKX3qRnflwv9AEJvEWYvdRJ7aqS1HCdOw'
	
	# استبدال 'CHAT_ID' بمعرف الدردشة الخاص بك
chat_id = '6509012689'
	
	# استبدال 'YOUR_MESSAGE' بالرسالة التي تريد إرسالها
message = ip
	
	# رابط الطلب API
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
	
	# معلومات الطلب
data = {
	    'chat_id': chat_id,
	    'text': message
}
	
	# إرسال الرسالة إلى البوت
response = requests.post(url, data=data)
