#real
import requests, random, time , colorama ,sys , fade 
from colorama import Fore
from dhooks import Webhook 

def logo():
    colorama.deinit()

    for char in banner:
        time.sleep(0.004)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("TurkyDH" )
banner = fade.water("""

 

 
████████╗██╗   ██╗██████╗ ██╗  ██╗██╗   ██╗██████╗ ██╗  ██╗
╚══██╔══╝██║   ██║██╔══██╗██║ ██╔╝╚██╗ ██╔╝██╔══██╗██║  ██║
   ██║   ██║   ██║██████╔╝█████╔╝  ╚████╔╝ ██║  ██║███████║
   ██║   ██║   ██║██╔══██╗██╔═██╗   ╚██╔╝  ██║  ██║██╔══██║
   ██║   ╚██████╔╝██║  ██║██║  ██╗   ██║   ██████╔╝██║  ██║
   
 
 

    +------------------------------------+------------------------------------------------------------+
    |             Vanity Cecker                    |                            Turky             |
    +====================================+============================================================+
    |          link insta :   860a_    |                         By : Al Britany 1975        |
    +------------------------------------+------------------------------------------------------------+
     
""")

logo()


proxy_servers = { # اذا عندك بروكسيات ضيفها بنفس طريقة
    'http': '117.160.250.137:8081',
    'http': '103.104.214.221:8080',
    'http': '221.132.18.38:80',
    'http': '138.197.102.119:80',
    'http': '140.238.210.181:80',
    'http': '170.187.138.40:8009',
    'http': '107.173.122.188:8080',
    'http': '103.145.113.78:80',
    'http': '81.250.223.126:80',
    'http': '217.52.247.75:1976',
    'http': '62.193.108.143:1976',
    'http': '103.111.122.2:80',
    'http': '204.137.250.6:3129',
    'http': '42.2.156.79:80',
    'http': '13.209.156.241:80',
    'http': '41.74.91.244:80',
    'http': '147.139.45.161:80',
    'http': '123.163.52.24:9091',
    'http': '45.79.17.203:80',
    'http': '112.98.177.27:9091',
    'http': '36.80.207.191:8080',
    'http': '61.158.175.38:9002',
    'http': '39.103.207.127:443',
    'http':  '118.31.2.38:8999',
    'http':  '183.234.218.195:9002',
    'http':  '183.64.239.19:8060',
    'http':  '115.219.85.131:8060',
    'http':  '8.210.127.228:8888',
    'http':  '117.160.250.163:9999',
    'http':  '188.235.130.50:8080',
    'http':  '103.216.49.133:32650',
    'http':  '121.18.224.54:9002',
    'http':  '45.189.118.92:999',
    'http':  '167.114.4.18:8050',
    'http':  '113.208.119.142:9002',
    'http':  '111.225.152.16:8089',   
 
}

error = 0
while True:
    user = "" 
    time.sleep(1) # كل عشرين ثانيه يفحص يفضل تخليها كل دقيقه

   # random في حال تبغى الفحص على ارقام فقط شيل الاحروف الي بفونكشن 
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=2): # 3 في حال تبغى الفحص يكون على ثلاثيات غير القيمة الى 
        user = user + character
        

 
    response = requests.get(f"https://discord.com/api/v9/invites/{user}",proxies=proxy_servers)
    
    if (response.status_code == 200):
        error += 1
        print(Fore.RED + f"NOT FOUND: {user}" + Fore.RESET)
        print( error ) 

        
   

    elif (response.status_code == 404):
        print(Fore.GREEN + f"USER FOUND : {user}" + Fore.RESET)
        #print(f"USER FOUND : {user} " )
        Special = Webhook("https://canary.discord.com/api/webhooks/1142107427282616320/nAz_4h9PiPFHKR7EyrSJbb1DDrI-RuaGSdxNcMu-x7D-bhB0jdGdNX9Er8z8WqFilJl8")

        #    في حال تبي تضيف ويب هوك  للسيرفرات ثانية او بنفس سيرفرك كرر نفس العملية الي تحت 

        #Special1 = Webhook("") 

       
        data =(user)
        Special.send(F"**Free Vanity : `{user}` <a:99uf48:1030438397782794330>**")

        #Special1.send(F"**Free Vanity : `{user}` <a:99uf48:1030438397782794330>**")

    else:
        print("Error") # اذا انطبع الايرور هاذا البروكسيات انحرقت
