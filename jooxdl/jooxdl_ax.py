import json,time,base64,re
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession
s= FuturesSession()
url_joox = re.compile('https?:\\/\\/.+')
class other_tool:
    def __init__(self,
                 mod:bool=False,
                 lang:str="en".lower()
                 ) -> None:
        if mod:
            print("\033[1;32;40m[DeBug] Start.DebugMod")
            print("\033[1;32;40m[DeBug] Start.main-function")
    class Debug():
        def __init__(self) -> None:
            self.lang='en'
            self.num=0
            self.wls={
                'en':' strat: functon - {}',
                "th":'เริ่มการทำงาน: ฟังก์ชั่น - {} '
                
            }
            self.wle={
                'en':' end  : functon - {}',
                "th":' จบการทำ    : ฟังก์ชั่น - {}'
                
            }
        def __call__(self,func) -> None:
                color="\033[1;32;40m"
                def new(ax,*val):
                    if ax.debug:
                        if self.num ==1:
                            ax.debug_lang
                            print(color,"[DeBug] function.start",self.wls[ax.debug_lang].format(func.__name__))
                            valre=func(ax,*val)
                            print()
                            print(color,"[DeBug] function.end  ",self.wle[ax.debug_lang].format(func.__name__))
                            return valre
                        else:
                            print(color,"[DeBug] function.start",self.wls[ax.debug_lang].format(func.__name__))
                            valre=func(ax,*val)
                            print(color,"[DeBug] function.end  ",self.wle[ax.debug_lang].format(func.__name__))
                            return valre
                        
                    else:
                        valre=func(ax,*val)
                        return valre
                    self.num+=1
                    
                return new
    @staticmethod
    def seconds2hms(seconds:int=0):
            """seconds2hms

            Args:
                seconds (int, optional): time sec. Defaults to 0.

            Returns:
                str : return time
            """
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return '%02d:%02d:%02d' % (h, m, s)

class url:
    def __init__(self,key) -> None:
        super().__init__()
        self.key=key
    @other_tool.Debug()
    def __sche_id(self,item):
        params = {
                        'songid': item,
                        'lang': 'th',
                        'country': 'th',
                        'from_type': '-1',
                        'channel_id': '-1',
                        '_': str(int(time.time()*1000))
                    }
        r = s.get('https://api.joox.com/web-fcgi-bin/web_get_songinfo', headers=self.headers1, params=params)
        ra = r.result()
        response = ra.content.decode('utf-8')
        response_json = json.loads(response.replace('MusicInfoCallback(', '')[:-1])
        
        for q_key in [('r320Url', '320'), ('r192Url', '192'), ('mp3Url', '128')]:
            download_url = response_json.get(q_key[0], '').replace(" ", "")
            if not download_url: continue
            filesize = str(round(int(json.loads(response_json['kbps_map'])[q_key[1]])/1024/1024, 2)) + 'MB'
            ext = 'mp3' if q_key[0] in ['r320Url', 'mp3Url'] else 'm4a'
            response = s.get('https://api-jooxtt.sanook.com/web-fcgi-bin/web_lyric', headers=self.lyric_headers, params=params)
            response =response.result()
            lyric = base64.b64decode(response.json().get('lyric', '')).decode('utf-8')
            #duration = int(download_url['play_duration'])
            songinfo = {
                            'album_url':response_json.get('malbummid', '-'),
                            'source': 'joox',
                            'songid': response_json.get('msingerid', '-'),
                            'singers': response_json.get('msinger', '-'),
                            'album': response_json.get('malbum', '-'),
                            'songname': response_json.get('msong', '-'),
                            'savename': response_json.get('msong', f'{self.key}_{int(time.time())}'),
                            'download_url': download_url.replace(" ", ""),
                            'lyric':lyric,
                            'filesize': filesize,
                            'ext': ext,
                            'duration': None,
                            'sec_duration':None,
                    }
            self.ls.append(songinfo)
        return self.ls
    
    @other_tool.Debug()
    def __req(self)->BeautifulSoup:
        
        response = s.get(self.key)
        r = response.result()
        response = r.content
        soup = BeautifulSoup(response, 'html.parser')
        Type=soup.find('meta',{"property":"og:type"})
        if Type == None:
            self.__Type="other"
        else:
            self.__Type=Type.attrs['content']
        return soup
    @other_tool.Debug()
    def __shc(self,soup):
        id=soup.find_all('link',{"hreflang":"x-default"})
        self.__id=id[0].attrs['href'].replace("https://www.joox.com/th/single/", "")[:-17]
    def __sche_playlist(self,soup):  
        
        for item in soup.find_all("b"):
            for item in item.find_all("a"):
                song=self.__sche_id(item.attrs['href'].replace("/th/single/", ""))
                self.arry.append(song)
        return  self.arry
    @other_tool.Debug()
    def __sche_other(self,soup):  
        for item in soup.find_all("span"):
            for item in item.find_all("span"):
                for item in item.find_all("a"):
                    print(item)
                    song=self.__sche_id(item.attrs['href'].replace("/th/single/", ""))
                    self.arry.append(song)
        return  self.arry
    @other_tool.Debug()
    def __sche_album(self,soup):  
        for item in soup.find_all("span"):
            for item in item.find_all("span"):
                for item in item.find_all("a"):
                    print(item)
                    song=self.__sche_id(item.attrs['href'].replace("/th/single/", ""))
                    self.arry.append(song)
        return  self.arry
    @other_tool.Debug()
    def __sche_vido(self,soup):  
        for item in soup.find_all("link",{'rel':"canonical"}):
            a=item.attrs['href']
                    
        return  a
    {
        "type":{
            "music.song",
            "playlist",
            "album",
            "video",
            "other"
            }
    }
    @other_tool.Debug()
    def __check_Type(self):
        suop=self.__req()
        if self.__Type =="music.song":
            self.__shc(suop)
            return self.__sche_id(self.__id)
        elif self.__Type =="playlist":
            return self.__sche_playlist(suop)
        elif self.__Type =="chart":
            return self.__sche_other(suop)
        elif self.__Type =="album":
            return self.__sche_album(suop)
        elif self.__Type =="video":
            return self.__sche_vido(suop)
        else:
            print(self.__Type)
    @other_tool.Debug()     
    def _main_url(self):
        
        return self.__check_Type()
        
class jooxdl:
    """HOW TO TI WORk \n
        [1] call function _main() | เรียก function _main() \n
        [2] call function __sech() && returns dict | เรียก function __sech() && returns dict\n
        [3] call function __find(dict from function) && returns dict to _main \n
            เรียก function __find(dictจากfunction__sech) && returns dict ถึง function _main\n
        [4] and function _main return dict from function __find to function main in class rs \n
            และ function _main return dict จาก function __find ถึง function main ใน class rs
        [5] END \n
    
    
    """
    def __init__(self) -> None:
        super().__init__()
    @other_tool.Debug()
    def __sech(self)->dict:
        """search music
            ค้นหาเพลง

        Returns:
            dict: return dict
        """
        response = s.get(f'https://api-jooxtt.sanook.com/openjoox/v2/search_type?country=th&lang=th&key={self.key}&type=0',headers=self.headers)
        r = response.result()
        response = r.content.decode('utf-8')
        json_data = json.loads(response)
        
        return json_data
    @other_tool.Debug()
    def _main(self)-> list:
        """mian
        
        Returns:
            dict: return dict from __find
        """
        return self.__find(self.__sech())
    @other_tool.Debug()
    def __find(self,json_data:dict):
            """find music && arrange info
                หาลิ้งsteamเพลง && จัดเรียงข้อมูล
            Args:
                json_data (dict): get from function __sech | รับจากfunction __sech

            Returns:
                dict: returns the sorted data | return ข้อมูลที่จัดเรียงแล้ว
            """
            try:
                for item in json_data['tracks']:
                    params = {
                            'songid': item[0]["id"],
                            'lang': 'th',
                            'country': 'th',
                            'from_type': '-1',
                            'channel_id': '-1',
                            '_': str(int(time.time()*1000))
                        }
                    r = s.get('https://api.joox.com/web-fcgi-bin/web_get_songinfo', headers=self.headers1, params=params)
                    ra = r.result()
                    response = ra.content.decode('utf-8')
                    response_json = json.loads(response.replace('MusicInfoCallback(', '')[:-1])
                    if response_json.get('code') != 0: continue
            except Exception as e: print(e)
            
            for q_key in [('r320Url', '320'), ('r192Url', '192'), ('mp3Url', '128')]:
                download_url = response_json.get(q_key[0], '').replace(" ", "")
                if not download_url: continue
                filesize = str(round(int(json.loads(response_json['kbps_map'])[q_key[1]])/1024/1024, 2)) + 'MB'
                ext = 'mp3' if q_key[0] in ['r320Url', 'mp3Url'] else 'm4a'
                response = s.get('https://api-jooxtt.sanook.com/web-fcgi-bin/web_lyric', headers=self.lyric_headers, params=params)
                response =response.result()
                lyric = base64.b64decode(response.json().get('lyric', '')).decode('utf-8')
                duration = int(item[0]['play_duration'])
                songinfo = {
                            'album_url':response_json.get('malbummid', '-'),
                            'source': 'joox',
                            'songid': str(item[0]['id']),
                            'singers': item[0]['artist_list'][0]['name'],
                            'album': response_json.get('malbum', '-'),
                            'songname': response_json.get('msong', '-'),
                            'savename': response_json.get('msong', f'{self.key}_{int(time.time())}'),
                            'download_url': download_url.replace(" ", ""),
                            'lyric':lyric,
                            'filesize': filesize,
                            'ext': ext,
                            'duration': self.seconds2hms(duration),
                            'sec_duration': duration,
                    }
                self.ls.append(songinfo)
            return ['Not found'] if self.ls ==[] else self.ls
    
class rs(
        url,
        jooxdl,
        other_tool,
        other_tool.Debug
        ):
    def __init__(
        self,
        key:str=None,
        debug:bool=False,
        debug_lang:str='en'.lower()
        ) -> None:
        
        self.__var()
        self.debug=debug
        self.debug_lang=debug_lang
            
            
        if key==None:
            raise ValueError
        elif url_joox.match(key):
            self.a=True

        else:
            self.a=False
        self.key=key
    
    def main(self)->list:
        self.AxDebug=other_tool(
            self.debug,
            self.debug_lang
                           )
        if self.a:
            return self._main_url() 
        else: 
            return self._main() 
    def __var(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'th,en-US;q=0.7,en;q=0.3',
            'Connection': 'keep-alive',
            'Host': 'api-jooxtt.sanook.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko)'
        }
        self.headers1 = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko)',
            'Cookie': 'wmid=142420656; user_type=1; country=id; session_key=2a5d97d05dc8fe238150184eaf3519ad;',
            'X-Forwarded-For': '36.73.34.109'
        }
        self.lyric_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Origin': 'https://www.joox.com'
        }
        self.ls=[]
        self.arry=[]