
import requests
from bs4 import BeautifulSoup

# gkatn
# input: URL
# output : 제목, 본문

# 원래 기존 함수 : 제목함수, 본문함수 따로
# - 이유: 함수를 만들 때는 하나의 함수에 다수의 기능을 넣기 X
def get_news_title_and_content(url):

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    # contents.pop(-1)
    for tag in contents:
        content = content + tag.get_text()
    return title, content