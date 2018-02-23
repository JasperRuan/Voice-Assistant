import function as func
from SpeechReconition import speech_recognition
from command_mode import command_mode

computer_name = 'Monday'
shut_down_command = ['goodby', 'bye', 'Bye', 'byebye', 'see you', 'See you']
thank_command = ['cheers', 'Cheers', 'thanks', 'Thanks', 'thank you', 'Thank you']
continue_programme = True
while continue_programme:
    text = speech_recognition()
    word = text.split(' ')
    if word[0].lower() == computer_name.lower():
        command_mode(word[1:], text)
    elif (word[0].lower() == 'hi' or word[0].lower() == 'hey') and word[1].lower() == computer_name.lower():
        command_mode(word[1:], text)
    else:
        print(text)

    for item in shut_down_command:
        if item in text:
            for element in thank_command:
                if element in text:
                    func.you_are_welcome()
            func.bye()
            continue_programme = False
