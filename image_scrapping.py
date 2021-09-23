import requests
import concurrent.futures
from bs4 import BeautifulSoup
import time


# t1=time.perf_counter()

# def get_article_image():  # scrap the targeted website and return desired data in a tuple form
#     url = "https://www.boursedirect.fr/fr/actualites/flux/aujourdhui"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
#     }
#     page = requests.get(url, headers=headers)
#     soup = BeautifulSoup(page.content, "html.parser")
#     counter=0
#     for img_news in soup.find_all("img", "img-responsive",width=True):
#         counter+=1
#         img_news_link='https://www.boursedirect.fr'+img_news['src']
#         with open('img_articles/'+str(counter)+'.jpg', 'wb') as f:
#             f.write(requests.get(img_news_link).content)

def get_article_image():  # scrap the targeted website and return desired data in a tuple form
    url = "https://www.boursedirect.fr/fr/actualites/flux/aujourdhui"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    img_news_link=[]
    counter=range(20)
    for img_news in soup.find_all("img", "img-responsive",width=True):
        img_news_link.append('https://www.boursedirect.fr'+img_news['src'])
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image,img_news_link,counter)

def download_image(img_url,num):
    with open('img_articles/'+str(num+1)+'.jpg', 'wb') as f:
        f.write(requests.get(img_url).content)



if __name__=="__main__":
    get_article_image()

# t2=time.perf_counter()
# print(f'Finished in {t2-t1} seconds')