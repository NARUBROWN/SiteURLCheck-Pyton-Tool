from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError

usrBaseURL = input("베이스 URL을 입력해주세요: ")
usrURL = input("전체 URL을 입력해주세요: ")
usrTag = input("찾고싶은 태그를 입력해주세요: ")
usrAtr = input("찾고싶은 태그의 속성을 입력해주세요: ")

html_test = urllib.request.Request(usrURL, headers={
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/44.0.2403.157 Safari/537.36"
})

html = urllib.request.urlopen(html_test)
soup_jeiu = BeautifulSoup(html, 'html.parser')

attr = soup_jeiu.select(f'{usrTag}')

href = ""

for i in attr:
    if bool(i[f'{usrAtr}']):
        print(f"\n{usrTag}태그의 텍스트: {i.getText()}")
    else:
        print(f"\n{usrTag}태그에 텍스트가 없습니다")

    if not i[f'{usrAtr}']:
        print("내용이 비어있음\n")
        continue
    elif i[f'{usrAtr}'][0] == "/":
        href = usrBaseURL + i[f'{usrAtr}']
        try:
            newname = urllib.request.urlopen(href, timeout=20)
            print(href, "| 연결이 정상 입니다.\n")
        except urllib.error.URLError as e:
            err = e.reason
            print(href, "| 연결이 불량 입니다.", err, "\n")
    elif not i[f'{usrAtr}'].find('http'):
        try:
            myname = urllib.request.urlopen(i[f'{usrAtr}'], timeout=20)
            print(i[f'{usrAtr}'], "| 연결이 정상 입니다.\n")
        except urllib.error.URLError as e:
            err = e.reason
            print(i[f'{usrAtr}'], "| 연결이 불량 입니다.", err, "\n")
    else:
        result = i[f'{usrAtr}']
        print("속성 | " + usrAtr + ": " + result)

