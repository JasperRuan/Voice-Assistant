import back_end
from speak import speak

def greeting():
    text = 'Hello sir'
    speak(text)

def tell_time():
    text = back_end.tell_time()
    speak(text)

def yes_sir():
    text = 'Yes, sir.'
    speak(text)

def find_wiki(keyword):
    text = back_end.get_wiki(keyword)
    speak(text)

def good_night():
    text = 'Good night sir'
    speak(text)

def time_to_go_to_bed():
    text = "It's time to go to bed."
    speak(text)

def wake_up():
    text = "Sir, it's time to get up."
    speak(text)

def tell_weatehr():
    now, min, max, weather = back_end.get_weather()
    text = "It's," + now + 'degrees now. The weather is' + weather
    speak(text)

def download_image(keyword, num):
    back_end.download_google_image(keyword, num)

def bye():
    speak('See you sir')
def you_are_welcome():
    speak('You are welcome')
