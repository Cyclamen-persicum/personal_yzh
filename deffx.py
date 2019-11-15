import requests,bs4,sys,os,time
#####   dataWrite用于检测是否正常获取页面
#####   dataAddress为存放网页数据的相对路径
#####   storageName为存放数据的文件名，略去后缀
#####   writeData存放抓取的网页数据
def dataWrite(dataAddress,storageName,writeData):
    os.chdir(dataAddress)
    data=open('.\\'+storageName+'.txt','w',encoding='utf-8')
    data.write(writeData)
    data.close()
#####   webRequset作用是获取目标页面上的特定信息
#####   url存放所要获取信息的页面
#####   cookie确保页面能够正常获取，若不存在写0
#####   header用于验证获取网页身份，若不存在写0
#####   grabStr为要在目标页面上获取的元素
#####   userMark为自定义标签
def webRequest(url,cookie,webHeader,grabStr,userMark):
    try:
        if not (webHeader==0 and cookie==0):
            webCookies={}
            for dataBlock in cookie.split(';'):
                name,value=dataBlock.strip().split('=',1)
                webCookies[name]=value  
            answer_Res=requests.get(url,cookies=webCookies,headers=webHeader)
        else:
            answer_Res=requests.get(url)
        answer_Res.encoding='utf-8'
        answerRes=answer_Res.text
        background=bs4.BeautifulSoup(answerRes,'lxml')
        dataWeb=background.select(grabStr)
        statusStr=[status.get_text() for status in dataWeb]
        print(userMark+' '+str(statusStr[0]).strip('\n'))
    except Exception:
        return