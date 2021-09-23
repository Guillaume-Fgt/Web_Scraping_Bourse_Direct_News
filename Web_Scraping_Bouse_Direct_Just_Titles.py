import requests
from bs4 import BeautifulSoup

txt_path_Title = "Web_Scraping_Bouse_Direct.txt"
txt_path_Hyperlinks = "Web_Scraping_Bouse_Direct_Hyperlinks.txt"

def update_txt_file(data, file_name):  # write data to a text file
    with open(file_name, "a",encoding='utf-8') as f:
        f.write(data + "\n")


def clean_txt_file(file_name):
    open(file_name, "w",encoding='utf-8').close()


def get_page_html():  # scrap the targeted website and return desired data in a tuple form
    clean_txt_file(txt_path_Title)
    clean_txt_file(txt_path_Hyperlinks)
    url = "https://www.boursedirect.fr/fr/actualites/flux/aujourdhui"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    #Titles
    ##############
    for title_news in soup.find_all("h2", "timeline-title"):
        update_txt_file(title_news.text,txt_path_Title)
    ##############
    
    #Hyperlinks
    ##############
    list_urls=[]

    for title_news in soup.find_all("div", "timeline-body"):
        links = title_news.findAll("a", href=True)
        for el in links:
             list_urls.append("https://www.boursedirect.fr" + str(el["href"])),  # hyperlink

    for list_url in list_urls:
        update_txt_file(list_url,txt_path_Hyperlinks)
    ##############

if __name__=="__main__":
    get_page_html()
