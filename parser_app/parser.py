import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = "https://kloop.kg/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}


# start parsing
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    container = soup.find_all("div", class_="elementor-posts-container")[3]
    items = container.find_all("article", class_="elementor-post")
    news = []
    for item in items:
        news.append(
            {
                'title_name': item.find('h3', class_="elementor-post__title").get_text(),
                'title_url': URL + item.find("h3", class_="elementor-post__title").find('a').get("href"),
                'image': URL + item.find('img').get('src'),

            }
        )
    return news


# endparsing
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news2 = []
        for page in range(0, 1):
            html = get_html(f'https://kloop.kg/', params=page)
            news2.extend(get_data(html.text))
        # print(news2)
        return news2

    else:
        raise Exception('Error in parser')

# parser()