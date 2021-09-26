from kivy.config import Config
Config.set('graphics', 'width', '530')
Config.set('graphics', 'height', '700')

from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from image_scrapping import get_article_image
from Web_Scraping_Bouse_Direct_Just_Titles import get_page_html
from kivymd.uix.chip import MDChip
import webbrowser


class MDGridLayoutNews(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        refresh_news(self)

    def refresh(self):
        self.clear_widgets()
        get_article_image()
        get_page_html()
        refresh_news(self)


class NewsApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style='Dark'
        pass


def refresh_news(self):
    try:
        for i in range(1, 21):
            img = Image(source='img_articles/'+str(i)+'.jpg',
                        allow_stretch=True, size_hint=(1, None),
                        height='248dp', nocache=True)
            self.add_widget(img)
            with open('Web_Scraping_Bouse_Direct.txt', 'r',
                      encoding="utf-8")as file:
                label_title = MDLabel(text=file.readlines()[i-1])
                self.add_widget(label_title)
            with open('Web_Scraping_Bouse_Direct_Hyperlinks.txt', 'r',
                      encoding="utf-8")as file:
                link_url = file.readlines()[i-1]
                link_widget = MDChip(text='link', icon='link',
                                     text_color='white', icon_color='white',
                                     radius=[1, ], on_press=lambda widget,
                                     link_url_inner=link_url:
                                     webbrowser.open(url=link_url_inner))
                self.add_widget(link_widget)
    except IndexError:
        self.clear_widgets()


if __name__ == "__main__":
    NewsApp().run()
