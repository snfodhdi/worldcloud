import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_news():
    """뉴스 제목 가져오기"""
    url = "https://www.bigkinds.or.kr/v2/news/search.do;Bigkinds=482D2818FAF321D74DDBB38965A5E017.tomcat2"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = []
    for link in soup.find_all('a'):
        text = link.get_text().strip()
        if len(text) > 3:
            titles.append(text)
    
    return titles

print("뉴스 크롤링 중...")
titles = get_news()
print(f"총 {len(titles)}개 제목 수집")

def make_wordcloud(titles):
    """워드클라우드 만들기"""
    text = " ".join(titles)

    exclude_words = [
        '뉴스', '일보', '신문', '데일리'
    ]
    
    wordcloud = WordCloud(
        font_path='malgun.ttf',
        width=800, 
        height=600,
        background_color='white',
        stopwords=exclude_words,
        max_words=100,
        min_font_size=10 
    ).generate(text)
    
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title('뉴스 제목 워드클라우드')
    plt.show()

print("워드클라우드 생성 중...")
make_wordcloud(titles)
print("완료!")