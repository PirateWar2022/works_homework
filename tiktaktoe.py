import random
import sre_parse
from tkinter import *
import random as r
import time as t
from PIL import ImageTk, Image

bul = False

class Menu(Tk):
    def __init__(self):
        super().__init__()

        # Background
        self.img_open = Image.open('back2.gif')
        self.img_open = self.img_open.resize((1920, 1080), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img_open)
        self.label = Label(image=self.img)

        # Configure the root window
        self.title('Tic-tac-toe')
        self.geometry('1920x1080')
        self.attributes("-fullscreen", True)

        # Labels
        self.lab = Label(self.label, text='Tic-tac-toe', font='Candara 110',
                         bg='SkyBlue2', fg='Slategray1')
        self.modes = Label(self.label, text='Modes', font='Arial 17')

        # Buttons
        self.two_players = Button(self.label, text='   2 players   ', font='Arial 22',
                                  bg='DeepSkyBlue4', fg='snow',command=self.two_pl)

        self.play_with_bot = Button(self.label, text='   BOT   ', font='Arial 18',
                                    bg='DeepSkyBlue4', fg='snow')

        self.exit = Button(self.label, text='  Exit  ', font='Arial 14',
                           bg='DeepSkyBlue4', fg='old lace', command=self.exi)

        # Draw buttons and labels
        self.run_buts_labels()

    def run_buts_labels(self):
        self.label.place(x=0, y=0, relheight=1, relwidth=1)
        self.lab.place(x=426, y=60)
        #self.modes.place(x=212, y=60)
        self.two_players.place(x=660, y=290) # x=200, y=120
        self.play_with_bot.place(x=700, y=373) # x=208, y=75
        self.exit.place(x=723, y=450)

        mainloop()

    def exi(self):
        self.destroy()

    def bot_but(self):
        global bul
        bul = False
        self.destroy()
        window1 = Two

    def two_pl(self):
        global bul
        bul = True
        self.destroy()
        window1 = Two()






# def change_the_window():

configs = [None] * 9
move = 0


class Two(Tk):
    def __init__(self):
        super().__init__()

        # Background
        self.img_open = Image.open('b3.jpg')
        self.img_open = self.img_open.resize((1920, 1080), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img_open)
        self.label = Label(image=self.img)

        # Configurate of window
        self.attributes("-fullscreen", True)

        # Label
        self.mod_lab = Label(text='MODE\nTwo players')
        self.win_lose_label = Label(text='                   ', font='Arial 52')

        # Buttons
        self.menu = Button(text='    Back to menu    ', bg='LightSkyBlue4', font='Arial 21', command=self.go_t_m)
        self.restart = Button(text='    Restart game    ', bg='LightSkyBlue4', font='Arial 20', command=self.rest)
        self.exit = Button(text='   Exit   ', bg='LightSkyBlue4', font='Arial 21', command=self.exi)

        # Tic-tac-toe buttons
    
        self.btns = [Button(width=10, height=5, font='Arial 21 bold', bg='SkyBlue3',command=lambda x=i: self.push(x)) for i in range(9)]
        

        self.run_buts_labels_1()

    def push_and_bot(self):
        pass
    def push(self, x):
        global move
        global configs

        if move % 2 == 0:
            self.char = 'X'
        else:
            self.char = 'O'

        configs[x] = self.char
        self.btns[x].config(text=self.char, bg='white', fg='black', state='disabled')
        print(configs)
        move += 1
        self.win()


    def run_buts_labels_1(self):
        self.label.place(x=0, y=0, relheight=1, relwidth=1)
        self.win_lose_label.place(x=100, y=50)


        self.menu.place(x=140, y=250)
        self.restart.place(x=143, y=350)
        self.exit.place(x=198, y=450)

        x = 800
        y = 160
        count = 0

        for i in range(9):
            self.btns[i].place(x=x, y=y)
            x += 180
            count += 1
            if count == 3:
                y += 174
                x = 800
                count = 0

        mainloop()

    def rest(self):
        self.destroy()
        s_w = Two()

    def go_t_m(self):
        self.destroy()
        f_w = Menu()

    def exi(self):
        self.destroy()


    def win(self):
        global configs
        if configs[0] == 'X' and configs[1] == 'X' and configs[2] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[1].config(bg='red')
            self.btns[2].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[3] == 'X' and configs[4] == 'X' and configs[5] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[3].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[5].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[6] == 'X' and configs[7] == 'X' and configs[8] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[6].config(bg='red')
            self.btns[7].config(bg='red')
            self.btns[8].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[0] == 'X' and configs[3] == 'X' and configs[6] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[3].config(bg='red')
            self.btns[6].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[1] == 'X' and configs[4] == 'X' and configs[7] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[1].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[7].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[2] == 'X' and configs[5] == 'X' and configs[8] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[2].config(bg='red')
            self.btns[5].config(bg='red')
            self.btns[8].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[0] == 'X' and configs[4] == 'X' and configs[8] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[8].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[2] == 'X' and configs[4] == 'X' and configs[6] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN X       ', font='Arial 45')
            self.btns[2].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[6].config(bg='red')
            print('win')
            configs = [None] * 9

            # ------------------------------------
        
        if configs[0] == 'O' and configs[1] == 'O' and configs[2] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[1].config(bg='red')
            self.btns[2].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[3] == 'O' and configs[4] == 'O' and configs[5] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[3].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[5].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[6] == 'O' and configs[7] == 'O' and configs[8] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[6].config(bg='red')
            self.btns[7].config(bg='red')
            self.btns[8].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[0] == 'O' and configs[3] == 'O' and configs[6] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[3].config(bg='red')
            self.btns[6].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[1] == 'O' and configs[4] == 'O' and configs[7] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[1].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[7].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[2] == 'O' and configs[5] == 'O' and configs[8] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[2].config(bg='red')
            self.btns[5].config(bg='red')
            self.btns[8].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[0] == 'O' and configs[1] == 'O' and configs[2] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[1].config(bg='red')
            self.btns[2].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[0] == 'O' and configs[4] == 'O' and configs[8] == 'O':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O      ', font='Arial 45')
            self.btns[0].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[8].config(bg='red')
            print('win')
            configs = [None] * 9

        elif configs[2] == 'O' and configs[4] == 'O' and configs[6] == 'X':
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")

            self.win_lose_label.config(text='       WIN O       ', font='Arial 45')
            self.btns[2].config(bg='red')
            self.btns[4].config(bg='red')
            self.btns[6].config(bg='red')
            print('win')
            configs = [None] * 9

        elif None not in configs:
            for i in range(len(self.btns)):
                self.btns[i].config(state="disabled")
            self.win_lose_label.config(text='       DRAW       ', font='Arial 45')
            print('win')
            configs = [None] * 9


if __name__ == '__main__':
    first_window = Menu()

    #sec_window = Two()
