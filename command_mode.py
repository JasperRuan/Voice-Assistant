import function as func

def command_mode(word, text):
    if 'weather' in word:
        print('weather')
        func.tell_weatehr()

    elif 'time' in word:
        func.tell_time()
