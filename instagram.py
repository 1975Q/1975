import requests
import socket
import random
#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
id_tele = ('735055104')
token_bot = ('2002443519:AAGdrLRtKnB_H0kCG5KaFUco9G8rWTMasSA')
def gethip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(hostname)
    print(IPAddr)
def uch():
    ld = '\033[1;32m'
    f = '\033[1;35m'
    headers = {'HOST': 'www.instagram.com',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) InspectBrowser',
               'X-CSRFToken': 'TNZhAQCH8OaoK8F5oZNHJ5ZrkAlSmcMM',
               'X-Instagram-AJAX': 'cec4fe0d7efe',
               'X-IG-App-ID': '936619743392459'
               }
    a7rf = ("qqeerrttyyuuiiooppllkkjjhhggffddssaazzxxccvvbbnn11223344556677889900....____")
    while True:
        user = str("".join(random.choice(a7rf) for i in range(5)))
        url = f'https://www.instagram.com/{user}/'
        rq = requests.get(url, headers=headers)
        if rq.status_code == 200:
            tlg = (
                f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={id_tele}&text=\nuser insta :  @{user}\nBy Turky DH \nmy website : https://www.instagram.com/860a_?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw== \nتنويه قد يكون اليوزر مبند ')
            req = requests.post(tlg)
            print('\033[1;36m' " user found :" + user)
        elif rq.status_code == 404:
            print('\x1b[2;31m' + " user not found : " + user)

print('''\033[33m
                  _                                        _ 
████████╗██╗   ██╗ ██████╗  ██╗  ██╗██╗   ██╗
╚══██╔══╝██║   ██ ║██╔══██╗ ██║ ██╔╝╚██╗ ██╔╝
   ██║   ██║   ██║ ██████╔╝ █████╔╝  ╚████╔╝ 
   ██║   ██║   ██║ ██╔══██╗ ██╔═██╗   ╚██╔╝  
   ██║   ╚██████╔╝ ██║  ██║ ██║  ██╗   ██║    

 by Turky Al Bri6any 1975 \033[39m''')
print('''
\033[31m[01]\033[36m show my ip & hostname

\033[31m[02]\033[36m usurs

\033[31m[00]\033[36m about
''')
chinput = input('\033[35mselect number : \033[39m')
if chinput == '1':
    gethip()
elif chinput == '2':
    uch()
elif chinput == '00':
    print('''
    by Turky 
    my instagram : 860a_
    ''')         