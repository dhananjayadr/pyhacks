import requests
from bs4 import BeautifulSoup
from colorama import init as colorama_init
from colorama import Fore, Style

colorama_init()

def hnews(url):
    soup = BeautifulSoup(url.text, "html.parser")
    entries = soup.select(".titleline")
    print(f'\nHacker news latest top 10:')
    print(f'{ "=" * 64}')
    for n, news in enumerate(entries, start=1):
        news_link = news.findChild("a")
        print(f'\n{Fore.GREEN}{n}. {news_link.get_text()}{Style.RESET_ALL}')
        if n == 10: break
    
if __name__ == '__main__':
    url = requests.get("https://news.ycombinator.com/")
    hnews(url)
