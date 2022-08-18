#importet
from tkinter import *
import random
from tkinter import font

#window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Guri letra dhe gershera by @Iseld Muca')
root.config(bg ='seashell3')

#koka
Label(root, text = "Guri, Leter, Gershera", font='arial 20 bold', bg = 'seashell3').pack()


#Zgjedhja e perdoruesit
user_zgjedhje = StringVar()
Label(root, text= 'Zgjidh njeren: guri, leter, gershera', font='arial 15 bold', bg = 'seashell3').place(x=30,y=70)
Entry(root, font= 'arial 15', textvariable= user_zgjedhje , bg = 'antiquewhite2').place(x=90, y=130)


#Funksionet per te luajtur
Result = StringVar()

def luaj():
    #Zgjedhja e kompjuterit
    pc_zgjedhje = random.randint(1,3)
    if pc_zgjedhje == 1:
        pc_zgjedhje = 'guri'
    elif pc_zgjedhje == 2:
        pc_zgjedhje = 'leter'
    else:
        pc_zgjedhje = 'gershera'
    ###########################
    user_marrje = user_zgjedhje.get()
    if user_marrje == pc_zgjedhje:
        Result.set('barazim,te dy zgjodhet njesoj')
    elif user_marrje == 'guri' and pc_zgjedhje == 'leter':
        Result.set('ti humbe, kompjuteri zgjodhi letren')
    elif user_marrje == 'guri' and pc_zgjedhje == 'gershera':
        Result.set('ti fitove, kompjuteri zgjodhi gersheren')
    elif user_marrje == 'leter' and pc_zgjedhje == 'gershera':
        Result.set('ti humbe, kompjuteri zgjodhi gersheren')
    elif user_marrje == 'leter' and pc_zgjedhje == 'guri':
        Result.set('ti fitove, kompjuteri zgjodhi gurin')
    elif user_marrje == 'gershera' and pc_zgjedhje == 'guri':
        Result.set('ti humbe, kompjuteri zgjodhi gurin')
    elif user_marrje == 'gershera' and pc_zgjedhje == 'leter':
        Result.set('ti fitove, kompjuteri zgjodhi letren')
    else:
        Result.set('Invalid: zgjihd njeren nga -- guri,letra,gershera')

#funksion per reset
def Reset():
    Result.set("")
    user_zgjedhje.set("")

#funksion per exit
def Exit():
    root.destroy()

#Buton
Entry(root, font = 'arial 10 bold', textvariable = Result, bg = 'antiquewhite2', width = 50,).place(x=25, y =250)

Button(root, font = 'arial 10 bold', text = 'LUAJ', padx=5, bg = 'seashell4', command= luaj).place(x=170, y =190)

Button(root, font = 'arial 10 bold', text = 'RESET', padx=5, bg = 'seashell4', command= Reset).place(x=70, y =310)

Button(root, font = 'arial 10 bold', text = 'LARGOHU', padx=5, bg = 'seashell4', command= Exit).place(x=230, y =310)

root.mainloop()