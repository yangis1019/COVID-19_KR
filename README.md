# COVID-19_KR
코로나19 대한민국 확진자 수 등등을 질병관리본부 홈페이지( http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun= )에서 가져오는 프로그램.
# 사용법
1. pip를 통해 BeautifulSoup와 urllib를 설치한다.

2. 편집기로 main.py를 연다.

3. main.py를 알맞게 잘 가공해서 사용한다.

# 함수 목록
```data_infected()```: 확진자 수를 int형으로 반환합니다.

```data_healed()```: 완치(격리 해제)된 사람들의 수를 int형으로 반환합니다.

```data_death()```: 사망자 수를 int형으로 반환합니다.

```data_checking()```: 검사 중인 사람들의 수를 int형으로 반환합니다.

```get_global_img(path, name)```: 질병관리본부에서 제공하는 코로나19의 국제 감염 현황 이미지를 path 경로에 파일명은 name으로 다운로드합니다.

```get_blocked_country(path, name)```: 질병관리본부에서 제공하는 코로나19로 인한 한국인 입국 금지/제한 국가 명단 pdf를 path 경로에 파일명은 name으로 다운로드합니다.
