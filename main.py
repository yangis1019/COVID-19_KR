'''
COVID-19_KR v2.0
LICENSE: MIT
Copyright (C) 2020 yangis1019
'''
from urllib.request import urlopen, urlretrieve
from urllib import parse
from bs4 import BeautifulSoup

try:
    site = urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun=")
    resp = site.read()
    soup = BeautifulSoup(resp, "lxml")
    
    find = soup.find_all('table', class_='num')
    find = [each_line.get_text().strip() for each_line in find[:20]]
    img = soup.find_all('div', class_='box_image')

    #p_data = soup.find_all('p', class_='s_descript')
    data = find[0].split("\n")
except:
    print("질병관리본부 사이트 서버 오류. 잠시 후 다시 시도해주세요.")
    exit()

def data_infected():
    rawresult = ""
    for i in range(len(data[8])-2):
        rawresult += data[8][i]
    result = rawresult.replace(",", "")
    return int(result)

def data_healed():
    rawresult = ""
    for i in range(len(data[12])-2):
        rawresult += data[12][i]
    result = rawresult.replace(",", "")
    return int(result)

def data_death():
    rawresult = ""
    for i in range(len(data[16])-2):
        rawresult += data[16][i]
    result = rawresult.replace(",", "")
    return int(result)

def data_checking():
    rawresult = ""
    for i in range(len(data[20])-2):
        rawresult += data[20][i]
    result = rawresult.replace(",", "")
    return int(result)


def get_global_img(path, name):
    imgpath = "http://ncov.mohw.go.kr"
    for i in range(40, len(str(img[0]))):
        if str(img[0])[i] == "\"":
            break
        imgpath += str(img[0])[i]
    return urlretrieve(imgpath, path + name)

'''
def get_blocked_country(path, name):
    pdfpath = "http://ncov.mohw.go.kr"
    datpath = ""
    for i in range(33, len(str(p_data[0]))):
        if str(p_data[5])[i] == "\"":
            break
        datpath += str(p_data[5])[i]
    datpath = parse.quote(datpath)
    pdfpath += datpath
    return urlretrieve(str(pdfpath), path + name)
#입국제한국가 pdf 제공 중단으로 인한 코드 제거
'''
