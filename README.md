# COVID-19_KR
코로나19 대한민국 확진자 수 등등을 질본 홈폐이지(http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun=)에서 가져오는 프로그램.
# 사용법
1. pip를 통해 BeautifulSoup와 urllib를 설치한다.

2. 편집기로 main.py를 연다.

3. main.py를 알맞게 잘 가공해서 사용한다.

# 함수 목록
```data_infected()```: 확진자 수를 int형으로 반환합니다.

```data_healed()```: 완치(격리 해제)된 사람들의 수를 int형으로 반환합니다.

```data_death()```: 사망자 수를 int형으로 반환합니다.

```data_checking()```: 검사 중인 사람들의 수를 int형으로 반환합니다.
