import requests,bs4,sys,os,re,shelve
from citylistDic import cityListdic
def cityNamecheck(cityName,cityDic):
    return cityDic.get(cityName,0)
print("请输入要查询天气的地址:")
inputCityname=input()
if not cityNamecheck(inputCityname,cityListdic):
    print("错误，地区不存在，请检查后重试")
    os.system("pause")
    sys.exit()
cityNum=cityListdic[inputCityname]
url=r'http://www.weather.com.cn/weather1d/'+cityNum+r'.shtml'
answer_Res=requests.get(url)
answer_Res.encoding='utf-8'
answerRes=answer_Res.text
background=bs4.BeautifulSoup(answerRes,'lxml')
localWea=background.select('ul.clearfix li p.wea')
localWin=background.select('ul.clearfix li p.win span')
localTem=background.select('ul.clearfix li p.tem span')
weas=[wea.get_text() for wea in localWea]
tems=[tem.get_text() for tem in localTem]
wins=[win.get_text() for win in localWin]
winsDir=[win.get('title') for win in localWin]
print('今天白天的天气为：')
print(tems[0]+'℃'+'\t'+weas[0]+'\t'+winsDir[0]+wins[0])
print('今天夜间的天气为：')
print(tems[1]+'℃'+'\t'+weas[1]+'\t'+winsDir[1]+wins[1])
os.system("pause")
