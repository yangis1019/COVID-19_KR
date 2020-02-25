from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    site = urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun=")
    resp = site.read()
    soup = BeautifulSoup(resp, "lxml")
    
    find = soup.find_all('ul', class_='s_listin_dot')
    find = [each_line.get_text().strip() for each_line in find[:20]]
    
    data = find[0].split("\n")
except:
    print("질병관리본부 사이트 서버 오류. 잠시 후 다시 시도해주세요.")
    exit()

def data_infected():
    rawresult = ""
    for i in range(7, len(data[0])-1):
        rawresult += data[0][i]
    result = rawresult.replace(",", "")
    return int(result)

def data_healed():
    rawresult = ""
    for i in range(12, len(data[1])-1):
        rawresult += data[1][i]
    result = rawresult.replace(",", "")
    return int(result)

def data_death():
    rawresult = ""
    for i in range(6, len(data[2])-1):
        rawresult += data[2][i]
    result = rawresult.replace(",", "")
    return int(result)

def data_checking():
    rawresult = ""
    for i in range(7, len(data[3])-1):
        rawresult += data[3][i]
    result = rawresult.replace(",", "")
    return int(result)
