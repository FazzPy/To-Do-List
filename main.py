from tkinter import *
from pymongo import MongoClient

root = Tk()
root.geometry("700x500+400+150")
root.config(bg="#4A464A")
root.title("To-Do List")
root.iconbitmap("icon.ico")
root.resizable(width=False, height=False)

bgColor = "#4A464A"

# Kendi veritabanı linkinizi girmeniz gerekiyor

DATABASE_LINK = "mongodb+srv://<username>:<password>@fazztech.zpsm83s.mongodb.net/?retryWrites=true&w=majority" # MongoDB Link

client = MongoClient(DATABASE_LINK)
database = client["Database"]
todo = database["Yapılacaklar"]

def Ekle():
    görev = ENTRY1.get()
    veri = {"Yapılıcak":görev}
    todo.insert_one(veri)
    LISTE_SIL()
    LISTE_EKLE()

def Sil():
    görev = ENTRY1.get()
    veri = {"Yapılıcak":görev}
    todo.delete_one(veri)
    LISTE_SIL()
    LISTE_EKLE()

def LISTE_SIL():
    LABEL1.destroy()
    LABEL2.destroy()
    ENTRY1.destroy()
    BUTON1.destroy()
    BUTON2.destroy()
    list1.destroy()
    sb.destroy()

def LISTE_EKLE():
    global LABEL1
    global LABEL2
    global ENTRY1
    global BUTON1
    global BUTON2
    global list1
    global sb
    LABEL1 = Label(text="Fazz | To-Do List v0.1", bg=bgColor, fg="white", font="Arial 16")
    LABEL1.place(x=10, y=10)

    LABEL2 = Label(text="Yapılıcak : ", bg=bgColor, fg="white", font="Arial 16")
    LABEL2.place(x=10, y=300)

    ENTRY1 = Entry(bg="lightgray", font="Arial 16", fg="black")
    ENTRY1.place(x=120, y=300)
    ENTRY1.focus

    BUTON1 = Button(text="Ekle", bg="green", fg="white", font="Arial 16", command=Ekle)
    BUTON1.place(x=380, y=295)

    BUTON2 = Button(text="Sil", bg="green", fg="white", font="Arial 16", command=Sil)
    BUTON2.place(x=450, y=295)

    list1 = Listbox(bg="lightgray",width=110)
    list1.place(x=10, y=50)

    sb = Scrollbar(
        root,
        orient=VERTICAL
    )
    sb.place(x=675, y=50)

    list1.config(yscrollcommand=sb.set)
    sb.config(command=list1.yview)

    for i in todo.find({}, {"_id":0}):
        list1.insert(0, i)


LABEL1 = Label(text="Fazz | To-Do List v0.1", bg=bgColor, fg="white", font="Arial 16")
LABEL1.place(x=10, y=10)

LABEL2 = Label(text="Yapılıcak : ", bg=bgColor, fg="white", font="Arial 16")
LABEL2.place(x=10, y=300)

LABEL3 = Label(text="Not : Silmek için görevin ismini yazmanız gerektir.", bg=bgColor, fg="white")
LABEL3.place(x=10, y=350)

ENTRY1 = Entry(bg="lightgray", font="Arial 16", fg="black")
ENTRY1.place(x=120, y=300)
ENTRY1.focus

BUTON1 = Button(text="Ekle", bg="green", fg="white", font="Arial 16", command=Ekle)
BUTON1.place(x=380, y=295)

BUTON2 = Button(text="Sil", bg="green", fg="white", font="Arial 16", command=Sil)
BUTON2.place(x=450, y=295)

list1 = Listbox(bg="lightgray",width=110)
list1.place(x=10, y=50)

sb = Scrollbar(
    root,
    orient=VERTICAL
)
sb.place(x=675, y=50)

list1.config(yscrollcommand=sb.set)
sb.config(command=list1.yview)

for i in todo.find({}, {"_id":0}):
    list1.insert(0, i)

root.mainloop()