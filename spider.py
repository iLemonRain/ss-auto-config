import urllib.request
from bs4 import BeautifulSoup


def get_png():
    # 获取html
    html = urllib.request.urlopen(
        "https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"  # noqa: E501
    )

    # 解析图片src
    soup = BeautifulSoup(html, 'html.parser')
    img_src = soup.select_one("#wiki-body > div > p > img")['src']

    # 下载图片
    img_name = 'ss_accounts.png'
    urllib.request.urlretrieve(img_src, img_name)
    return img_name
