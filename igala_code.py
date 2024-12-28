
from tkinter import Entry, StringVar, Button , Tk
from tkinter.ttk import Label

window = Tk()
window.geometry("600x250")
window.title('Igala Dictionary')

entry_text = Entry(window)
entry_text.pack()

result=StringVar()
result_label = Label(window,textvariable=result)
result_label.pack()

Igala_dict = {
    'enu' : 'mouth : Part of the body used for speech and eating.' ,
    'ebole' : 'food : Something eaten to norish the body.' ,
    'oma' : 'child : A young human being.' ,
    'olojo' : 'sun : The celestial body that provides light and heat during the day.' ,
    'echo' : 'water : A liquid essential for life.' ,
    'egbon' : 'elder sibling : Older brother or sister.' ,
    'ojo' : 'day : A 24-hour period.' ,
    'ena' : 'part/road : A way or route for travelling.' ,
    'eko' : 'knoweledge/education : Learning or understanding something.' ,
    'ene' : 'person : A human being.' ,
    'ujo' : 'House : A place where people live.' ,
    'ekojo' : 'work : Acivity involving effort to produce result.' ,
    'elubi' : 'yam : A staple food.' ,
    'ebe' : 'ground : The surface of the earth.' ,
    'elele' : 'sky : The space above he earth.' ,
    'okuko' : 'chicken : A domesticated bird raised for food and eggs.' ,
    'efo' : 'leaf : Part of a plant, typically green.' ,
    'je' : 'eat : To consume food.' ,
    'mi' : 'drink : To consume liquid.' ,
    'kwu' : 'speak : To say words.' ,
    'ojoo' : 'bad : Something harmful or unpleasant. ' ,
    'omomi' : 'beautiful : Something pleasant to look at.'


}


def search(word):
    if word in Igala_dict:
        result.set(Igala_dict[word])
        print(Igala_dict[word])

    else:
        result.set('Not Found')


search_btn = Button(window, text='Search', command= lambda : search(entry_text.get()))
search_btn.pack()


#run the application
window.mainloop()
