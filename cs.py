import requests
from bs4 import BeautifulSoup
# 一.1.
def test1():

    url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
    rsp=requests.get(url)
    html=rsp.content
    with open('rq.html','wb') as f:
        f.write(html)
    print('ok')


def test12():
    x=BeautifulSoup(open('rq.html',encoding='utf8'),features='html.parser')
    title=x.find('title').text  #标题
    print(title)
    print(x.text)




def test13():
    with open('疫情.csv','w',encoding='utf8') as f:
        f.write('')

    # 由于其余数据是获得数据，单单从网址上无法获得，是需要跳转其他url来进行获取，
    # 查阅了csdn不知道如何获取

# 二
def test2():
    with open('cwd.txt','r') as f:
        messag=f.readlines()
    key={}
    fund={}
    s=[] #最外侧

    isin=[] #最里侧
    key['name']=messag[1]
    key['lei']=messag[2]

    i=3
    while i<len(messag):
        if messag[i][0].isdigit():
            s.append((fund))
            isin=[]
            fund={}
            fund['title']=messag[i][2:]
            i+=1
        else:
            isin.append(messag[i])
            fund['isin']=isin
            i+=1
    s.append(fund)
    key['sub_fund']=s[1:]
    print(key)




if __name__ == '__main__':
    test1()
    test2()
    test12()
    test13()