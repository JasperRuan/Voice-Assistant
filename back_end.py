import wikipedia
import requests
import time
from icrawler.builtin import GoogleImageCrawler

def get_weather():
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Auckland'
    json_data = requests.get(api_address).json()
    now = round(float(json_data['main']['temp']) - 273.15)
    min = round(float(json_data['main']['temp_min']) - 273.15)
    max = round(float(json_data['main']['temp_max']) - 273.15)
    weather = json_data['weather'][0]['main']
    return str(now), str(min), str(max), str(weather)

def get_wiki(string):
    text = wikipedia.summary(string, sentences=2)
    return text
def get_time():
    tim = time.strftime('%Y-%m-%d*%H:%M:%S', time.localtime(time.time()))
    year = tim[:tim.find('-')]
    month = tim[tim.find('-') + 1: tim.rfind('-')]
    date = tim[tim.rfind('-') + 1: tim.find('*')]
    hour = tim[tim.find('*') + 1: tim.find(':')]
    minute = tim[tim.find(':') + 1: tim.rfind(':')]
    second = tim[tim.rfind(':') + 1:]
    return year, month, date, hour, minute, second

def tell_time():
    year, month, date, hour, minute, second = get_time()
    text = "It's " + str(hour) + ' ' + str(minute)
    return text

def download_google_image(keyword, num):
    image_name = keyword
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': image_name})
    google_crawler.crawl(keyword=image_name, max_num=num,
                         date_min=None, date_max=None,
                         min_size=(200, 200), max_size=None)
