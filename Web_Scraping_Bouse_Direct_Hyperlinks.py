import requests
from bs4 import BeautifulSoup

txt_path_Hyperlinks = "Web_Scraping_Bouse_Direct_Hyperlinks.txt"


def update_txt_file(data):  # write data to a text file
    with open(txt_path_Hyperlinks, "a",encoding='utf-8') as f:
        f.write(data + "\n")


def clean_txt_file():
    open(txt_path_Hyperlinks, "w",encoding='utf-8').close()


def get_page_html():  # scrap the targeted website and return desired data in a tuple form
    url = "https://www.boursedirect.fr/fr/actualites/flux/aujourdhui"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    list_urls=[]

    for title_news in soup.find_all("div", "timeline-body"):
        links = title_news.findAll("a", href=True)
        for el in links:
             list_urls.append("https://www.boursedirect.fr" + str(el["href"])),  # hyperlink

    for list_url in list_urls:
        update_txt_file(list_url)


if __name__ == '__main__':
    get_page_html()


