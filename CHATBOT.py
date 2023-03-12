from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import speech_recognition as s
import threading




bot=ChatBot(" Prabhjot BOT")


convo=[


    "hi",
    "hello",
    "whats your name?",
    "i am bot prabhjot created ",
    "where do you live ",
    "i live in prabhjot laptop menory",
    "how old are you",
    " Prabhjot KNOWS",
    "how are you",
    "i am good how you doing?",
     "on which language you based on",
     "pyhton",
    " who are you",
    "i am bot do you like movies?",
    "yes",
    "which one is your favourite movie?",
    "spencer",
    "whhich language you like most?",
    "english and you?",
    " i liked pyhton because i am based on that ",
    "Do you know a joke?",
    "yes wanna hear it ",
    "yes",
    " What time is it when the clock strikes 13?"
    "i dont know",
    "Time to get a new clock hahahhaha",
    " your are funny boy",
    "thank you  wanna hear one more?",
    "yes",
    " What do you call two birds in love?",
    "i dont know",
    "Tweethearts",
    "hahahha",
    
]    

len(convo)


me=ListTrainer(bot)


me.train(convo)





main = Tk()

main.geometry("1000x700")

main.title("prabhjot  BOT")

main['background']='white'






def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")




def ask_from_bot():
    query = textF.get()
    answer_from_bot= bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
   
    textF.delete(0, END)
    msgs.yview(END)
    



frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=100, height=20 ,bg='black', fg='white', yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()





textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)



btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)




def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()




main.mainloop()