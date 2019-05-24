import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen(
    "https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"  # noqa: E501
)

soup = BeautifulSoup(html, 'html.parser')
img_src = soup.select_one("#wiki-body > div > p > img")['src']

urllib.request.urlretrieve(img_src, 'ss_accounts.png')