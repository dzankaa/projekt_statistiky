import tkinter
import time
from datetime import datetime, timedelta
import os

root = tkinter.Tk()
root.attributes('-fullscreen',True) # hlavne okno na celu obrazovku

c = tkinter.Canvas(root)
c.pack(fill=tkinter.BOTH, expand=True)

#na rusenie canvasu a velkost obrazovky
root.bind('<Escape>', lambda event: root.destroy())
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#..............DEFINICIE...............................
def zakl_nast():
    global w1_graf, w2_graf, h1_graf, h2_graf, ciara1, ciara2, mys
    c.delete('text', 'g3', 'g4ab','g4c')
    mys = False
    button.place(x=width//5*4, y=height//10)
    w1_graf = width//3
    w2_graf = width//4*3
    h1_graf = height//5*4
    h2_graf = height//7*2
    ciara1 = c.create_line(w1_graf, h1_graf , w2_graf, h1_graf, tags='menu2') #vodorovna ciara grafu
    ciara2 = c.create_line(w1_graf, h1_graf , w1_graf, h2_graf, tags='menu') #zvisla ciara grafu
    button_tyzden.place(x=-1000, y=0)
    button_dnes.place(x=-1000, y=0)
    button4a.place(x=-1000, y=0)
    button4b.place(x=-1000, y=0)
    button_nepredane.place(x=-1000, y=0)

#definicie obrazoviek
def zakladna(event = None):
    global aktual_obrazovka
    aktual_obrazovka = zakladna
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    c.delete('text', 'menu', 'g3', 'g4ab','g4c','menu2')
    button.place(x=-1000, y=-1000)
    obrazok = c.create_image(width//5*3, height//2, image=logo, tags='text')
    button_tyzden.place(x=-1000, y=0)
    button_dnes.place(x=-1000, y=0) 
    button4a.place(x=-1000, y=0)
    button4b.place(x=-1000, y=0)
    button_nepredane.place(x=-1000, y=0)

    
def prva(b1):
    global posledny_b, aktual_obrazovka
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b1['bg']=b1['activebackground']='#679222'
    posledny_b=b1
    aktual_obrazovka = prva
    zakl_nast()
    c.create_text(width//5*2, height//6, text='Najviac predávané tovary', font='Roboto 27', tags='text')
    pom_w = (w2_graf - w1_graf)/len(hodnoty1)
    pom_h = (h1_graf - h2_graf)/hodnoty1[0]
    a = 0
    for i in range(len(hodnoty1)):
        c.create_rectangle(w1_graf+pom_w*i+pom_w//6, h1_graf, w1_graf+pom_w*i+pom_w-pom_w//6, h1_graf-pom_h*hodnoty1[i],fill=('#e0da63'), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf-pom_h*int(hodnoty1[i])-(h1_graf-h2_graf)//15, text=str(hodnoty1[i]), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf+(h1_graf-h2_graf)//15, text=nazvy1[i], tags='text')
        c.create_text(width/5*4, height//3+a, text=nazvy1[i], font='Roboto 11', anchor='w', tags='text')
        c.create_text(width/10*9, height//3+a, text=str(hodnoty1[i]), font='Roboto 11', tags='text')
        a += height//17
        
def druha(b2):
    global posledny_b, aktual_obrazovka
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b2['bg']=b2['activebackground']='#679222'
    posledny_b=b2
    aktual_obrazovka = druha
    zakl_nast()
    c.create_text(width//5*2, height//6, text='Najmenej predávané tovary', font='Roboto 27', tags='text')
    if max(hodnoty2) == 0:
        pom_h = 0
        c.create_text(width/5*2, height/2, text='tieto položky \nsa nepredali \nani raz', font='Roboto 15', fill='#e0da63', tags='text')
    else:   
        pom_h = (h1_graf - h2_graf)/hodnoty2[0]
    pom_w = (w2_graf - w1_graf)/len(hodnoty2)
    a = 0
    for i in range(len(hodnoty2)):
        c.create_rectangle(w1_graf+pom_w*i+pom_w//6, h1_graf, w1_graf+pom_w*i+pom_w-pom_w//6, h1_graf-pom_h*hodnoty2[i],fill='#e0da63', tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf-pom_h*int(hodnoty2[i])-(h1_graf-h2_graf)//15, text=str(hodnoty2[i]), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf+(h1_graf-h2_graf)//15, text=nazvy2[i], tags='text')
        c.create_text(width/5*4, height//3+a, text=nazvy2[i], font='Roboto 11', anchor='w',tags='text')
        c.create_text(width/10*9, height//3+a, text=str(hodnoty2[i]), font='Roboto 11', tags='text')
        a += height//17
    if len(vobec_nepredane) > 10:
            button_nepredane.place(x=width//9*2, y=height//8*7, width=width/10)

def nepredane():
    okno = tkinter.Toplevel(root)
    okno.lift()
    okno.title('Nepredané tovary')
    okno.geometry('500x500')
    root.eval('tk::PlaceWindow {} center'.format(str(okno)))
    a = 0
    for j in range(len(vobec_nepredane)//24+1):
        i = 0
        while a != len(vobec_nepredane) and i < 24:
            tkinter.Label(okno, text=vobec_nepredane[i+24*j]).grid(row=i, column=j)
            i += 1
            a += 1

def tretia(b3):
    global pom_w3, pom_h3, hod3, nakup, posledny_b, mys, pom, aktual_obrazovka, aktual_graf
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b3['bg']=b3['activebackground']='#679222'
    posledny_b=b3
    aktual_obrazovka = tretia
    c.delete('g3')
    zakl_nast()
    button_tyzden.place(x=width//9*2, y=height//8*7, width=width//10)
    button_dnes.place(x=width//9*2, y=height//6*5, width=width//10)
    mys = True
    pom = 3
    c.bind('<Motion>', myska)
    c.create_text(width//5*2, height//6, text='Priemerná cena nákupu', font='Roboto 27', tags='text')
    a = height//20
    c.create_text(width//8*7, height//3, text=' aktuálna priemerná cena \n dnešných nákupov: ', font='Roboto 12', tags='text')
    c.create_text(width//9*8, height//3+a, text=str(round(hodnoty3tyzden[-1],2)), font='Roboto 11', tags='text')
    c.create_text(width//8*7, height//3+2*a, text='priemerné ceny nákupov \n za posledný týždeň:', font='Roboto 12', tags='text')
    if nakup:
        aktual_graf = dnes
        hod3 = hodnoty3den
        dopln = 'dnesny den'
        button_dnes['bg']=button_dnes['activebackground']='#aca932'
        button_tyzden['bg']=button_tyzden['activebackground']='#e0da63'
    else:
        aktual_graf = tyzden
        hod3 = hodnoty3tyzden
        dopln = 'posledny tyzden'
        button_tyzden['bg']=button_tyzden['activebackground']='#aca932'
        button_dnes['bg']=button_dnes['activebackground']='#e0da63'
    pom_w3 = (w2_graf - w1_graf)/len(hod3)
    pom_h3 = (h1_graf - h2_graf)/max(hod3)
    if (dnesne_nakupy != [0.001] or hod3 == hodnoty3tyzden) and max(hod3) != 0.001:
        graf3 = ()
        cisla = max(hod3)/5
        for i in range(5):
            c.create_oval(w1_graf-3, h1_graf-((h1_graf-h2_graf)/max(hod3))*cisla-3,w1_graf+3, h1_graf-((h1_graf-h2_graf)/max(hod3))*cisla+3, fill='black', tags='g3')
            c.create_text(w1_graf-width//80, h1_graf-((h1_graf-h2_graf)/max(hod3))*cisla, text=str(round(cisla,1)), tags='g3')
            cisla += max(hod3)/5    
        for i in range(len(hod3)):
            graf3 += (w1_graf+pom_w3*i+pom_w3//2, h1_graf-pom_h3*hod3[i])
            c.create_oval(w1_graf+pom_w3*i+pom_w3//2-3, h1_graf-pom_h3*hod3[i]-3, w1_graf+pom_w3*i+pom_w3//2+3, h1_graf-pom_h3*hod3[i]+3, fill='#aca932', outline='#aca932',tags='g3')
            a += height/20
        a = height/20
        c.create_text(width/2, h1_graf+h1_graf/10, text='pre zobrazenie konkrétnych hodnôt prejdi myšou cez body', font='Roboto 10', tags='text')
        if len(hod3) >1 :
            c.create_line(graf3, fill='#aca932', tags='g3')
        else:
            c.create_line(graf3, graf3[0], h1_graf, fill='#aca932', tags='g3')
    else:
            c.create_text(w2_graf-w1_graf, h1_graf-h2_graf, text='Nepredali sa \nzatiaľ žiadne tovary', font='Roboto 13', fill='#679222', tags='g3')
    for i in range(len(hodnoty3tyzden)):
            c.create_text(width//9*8, height//3+2*(height//20)+a, text=str(round(hodnoty3tyzden[i],2)), font='Roboto 11', tags='g3')
            c.create_text(width//7*6, height//3+2*(height//20)+a, text=str(datumy[i]), font='Roboto 11', tags='g3')
            a += height/20
    c.create_text(width/2, h1_graf+h1_graf/20, text='hodnoty nákupov za '+dopln, font='Roboto 15', tags='text')

      
def stvrta(b4):
    global posledny_b, aktual_obrazovka, ah, aktual_graf
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b4['bg']=b4['activebackground']='#679222'
    posledny_b=b4
    aktual_obrazovka = stvrta
    zakl_nast()
    mys = True
    button4b.place(x=width//9*2, y=height//8*7, width=width/10)
    button4a.place(x=width//9*2, y=height//6*5, width=width/10)
    if ah:
        aktual_graf = rozdiel
        rozdiel(event = None)        
    else:
        aktual_graf = naklad_trzba
        naklad_trzba(event = None)
    c.create_text(width//5*2, height//6, text='Aktuálne tržby a náklady', font='Roboto 27', tags='text')
    if max(hod4trzby) != 0 or  max(hod4naklady) != 0:
        c.create_text(width/2, h1_graf+h1_graf/20, text='pre zobrazenie konkrétnych hodnôt prejdi myšou cez body', font='Roboto 10', tags='text')
    hod4 = ['aktuálna tržba:', str(round(hod4trzby[-1],2)), 'aktuálne náklady:', str(round(hod4naklady[-1],2)), 'rozdiel:', str(round(hod4trzby[-1]-hod4naklady[-1],2))]
    a = height/20
    for i in range(6):
        c.create_text(width/7*6, height/5*2+a*i, text=hod4[i], font='Roboto 11', tags='text')
        
# definicie ku stvtej obrazovke
def naklad_trzba(event = None):
    global ciara1,pom,mys,pom_w4,pom_h4, aktual_graf, ah
    ah = 0
    c.delete('g4c')
    button4a['bg']=button_dnes['activebackground']='#aca932'
    button4b['bg']=button_tyzden['activebackground']='#e0da63'
    graf4a = ()
    graf4b = ()
    aktual_graf = naklad_trzba
    maxi = max(hod4trzby+hod4naklady)
    if max(hod4trzby) != 0 or  max(hod4naklady) != 0:
        pom_h4 = (h1_graf - h2_graf)/maxi
        pom_w4 = (w2_graf - w1_graf)/len(hod4trzby)
        c.create_line(w1_graf, h1_graf , w2_graf, h1_graf, tags='g4ab')
        cisla = maxi/5
        for i in range(5):
            c.create_oval(w1_graf-3, h1_graf-((h1_graf-h2_graf)/maxi)*cisla-3,w1_graf+3, h1_graf-((h1_graf-h2_graf)/maxi)*cisla+3, fill='black', tags='g4ab')
            c.create_text(w1_graf-width//80, h1_graf-((h1_graf-h2_graf)/maxi)*cisla, text=str(round(cisla,2)), tags='g4ab')
            cisla += maxi/5
        for i in range(len(hod4trzby)):
            graf4a += (w1_graf+pom_w4*i+pom_w4//2, h1_graf-(pom_h4*hod4trzby[i]))
            graf4b += (w1_graf+pom_w4*i+pom_w4//2, h1_graf-(pom_h4*hod4naklady[i]))
            c.create_oval(w1_graf+pom_w4*i+pom_w4//2-3, h1_graf-pom_h4*hod4trzby[i]-3, w1_graf+pom_w4*i+pom_w4//2+3, h1_graf-pom_h4*hod4trzby[i]+3, fill='#00701a', outline='#679222',tags='g4ab')
            c.create_oval(w1_graf+pom_w4*i+pom_w4//2-3, h1_graf-pom_h4*hod4naklady[i]-3, w1_graf+pom_w4*i+pom_w4//2+3, h1_graf-pom_h4*hod4naklady[i]+3, fill='#ffee58', outline='#aca932',tags='g4ab')
        c.create_line(graf4a, fill='#00701a', width=1, tags='g4ab')
        c.create_line(graf4b, fill='#ffee58', tags='g4ab')
        c.create_text(w2_graf-w2_graf/12, h1_graf+h1_graf/20, text='tržby', font='Roboto 10', tags='g4ab')
        c.create_text(w2_graf-w2_graf/12, h1_graf+h1_graf/10, text='náklady', font='Roboto 10', tags='g4ab')
        c.create_line(w2_graf, h1_graf+h1_graf/20, w2_graf-w2_graf/20 ,h1_graf+h1_graf/20, fill='#00701a', width=4, tags='g4ab')
        c.create_line(w2_graf, h1_graf+h1_graf/10, w2_graf-w2_graf/20 ,h1_graf+h1_graf/10, fill='#ffee58', width=4, tags='g4ab')
        mys = True
        pom = 4
        c.bind('<Motion>', myska)
    else:
        c.create_text(w2_graf-w1_graf, h1_graf-h2_graf, text='za posledný týždeň \nnemame ziadne udaje', font='Roboto 13', fill='#679222', tags='g4ab')
    
def rozdiel(event = None):
    global pom,mys,hod4roz,h4_graf,dielik, pom_w4, aktual_obrazovka, ah, aktual_graf
    ah = 1
    button4b['bg']=button_dnes['activebackground']='#aca932'
    button4a['bg']=button_tyzden['activebackground']='#e0da63'
    aktual_graf = rozdiel
    hod4roz = ()
    for i in range(len(hod4trzby)):
        hod4roz += (round(hod4trzby[i]-hod4naklady[i],2),)
    if max(hod4trzby) != 0 and max(hod4naklady) != 0:
        c.delete('g4ab', 'menu2')
    c.delete('g4ab')
    if max(hod4roz) == 0:
        c.create_text(w2_graf-w1_graf, h1_graf-h2_graf, text='všetky rozdiely sú nulové', font='Roboto 13', fill='#679222', tags='g4c')
    else:
        maxi = max(hod4roz)
        mini = min(hod4roz)
        dielik = (h1_graf - h2_graf)/(abs(maxi)+abs(mini))
        h4_graf = h1_graf-(abs(mini)*dielik)
        c.create_line(w1_graf, h4_graf , w2_graf, h4_graf, tags='g4c')
        pom_w4 = (w2_graf - w1_graf)/len(hod4trzby)
        graf4c = ()
        cisla = round(mini,2)
        for i in range(6):
            c.create_oval(w1_graf-3, h4_graf-dielik*cisla-3, w1_graf+3, h4_graf-dielik*cisla+3, fill='black', tags='g4c')
            c.create_text(w1_graf-width//80, h4_graf-dielik*cisla, text=str(round(cisla,2)), tags='g4c')
            cisla += round((abs(mini)+abs(maxi))/6,2)
        for i in range(len(hod4trzby)):
            graf4c += (w1_graf+pom_w4*i+pom_w4//2, h4_graf-(dielik*hod4roz[i]))
            c.create_oval(w1_graf+pom_w4*i+pom_w4//2-3, h4_graf-dielik*hod4roz[i]-3, w1_graf+pom_w4*i+pom_w4//2+3, h4_graf-dielik*hod4roz[i]+3, fill='#aca932', outline='#aca932',tags='g4c')
        c.create_line(graf4c, fill='#aca932', tags='g4c')
        mys = True
        pom = 5
        c.bind('<Motion>', myska)
    
# definicie k tretej obrazovke
def myska(suradnice):
    global popis
    if not mys:
        return None
    xm = suradnice.x
    ym = suradnice.y
    c.delete(popis)
    if pom == 3:
        for i in range(len(hod3)):
            if (w1_graf+pom_w3*i+pom_w3//2-10 <= xm <= w1_graf+pom_w3*i+pom_w3//2+10) and (h1_graf-pom_h3*hod3[i]-10 <= ym <= h1_graf-pom_h3*hod3[i]+10):
                if nakup:
                    pomocna = '\nčas: '+casy[i]
                else:
                    pomocna = '\ndátum: '+datumy[i]
                popis = c.create_text(w1_graf+pom_w3*i+pom_w3//2-10, h1_graf-pom_h3*hod3[i]-20, text='hodnota: '+str(round(hod3[i],2))+pomocna, font='Roboto 8', tags='g3')
                
    elif pom == 4:
        for i in range(len(hod4trzby)):
            if (w1_graf+pom_w4*i+pom_w4//2-10 <= xm <= w1_graf+pom_w4*i+pom_w4//2+10) and (h1_graf-pom_h4*hod4trzby[i]-10 <= ym <= h1_graf-pom_h4*hod4trzby[i]+10):
                popis = c.create_text(w1_graf+pom_w4*i+pom_w4//2-10, h1_graf-pom_h4*hod4trzby[i]-20, text='hodnota: '+str(round(hod4trzby[i],2))+'\ndátum: '+datumy[i], font='Roboto 8', tags='g4ab')
                
            elif (w1_graf+pom_w4*i+pom_w4//2-10 <= xm <= w1_graf+pom_w4*i+pom_w4//2+10) and (h1_graf-pom_h4*hod4naklady[i]-10 <= ym <= h1_graf-pom_h4*hod4naklady[i]+10):
                popis = c.create_text(w1_graf+pom_w4*i+pom_w4//2-10, h1_graf-pom_h4*hod4naklady[i]-20, text='hodnota: '+str(round(hod4naklady[i],2))+'\ndátum: '+datumy[i], font='Roboto 8', tags='g4ab')
    if pom == 5:
        for i in range(len(hod4roz)):
            if (w1_graf+pom_w4*i+pom_w4//2-10 <= xm <= w1_graf+pom_w4*i+pom_w4//2+10) and (h4_graf-dielik*hod4roz[i]-10 <= ym <= h4_graf-dielik*hod4roz[i]+10):
                popis = c.create_text(w1_graf+pom_w4*i+pom_w4//2-10, h4_graf-dielik*hod4roz[i]-20, text='hodnota: '+str(round(hod4roz[i],2))+'\ndátum: '+datumy[i], font='Roboto 8', tags='g4c')                
                                              
def dnes(event = None):
    global nakup, aktual_graf
    aktual_graf = dnes
    nakup = 1
    tretia(b3)

def tyzden(event = None):
    global nakup, aktual_graf
    aktual_graf = tyzden
    nakup = 0
    tretia(b3)

# datum a cas
def spusti_cas():
    global hodiny
    c.delete(hodiny)
    cas = time.strftime('%A %d.%b %Y %H:%M:%S', time.localtime())
    hodiny = c.create_text(width//9*8, height/30*29, text=cas)
    c.after(1000, spusti_cas) 

#..............DIZAJN A BUTTONY....................................

# nazov modulu a pozadia
c.create_rectangle(width//5, 0, width, height, fill='white', outline='white')
c.create_rectangle(0, 0, width//5, height, fill='#98c151', outline='#98c151')
c.create_line(width//5, height//15*14+1, width, height//15*14+1, fill='darkgrey', width=2)
c.create_line(width//5, 0, width//5, height, fill='darkgrey', width=2)
c.create_text(width//10, height//6, text='Štatistiky', font='Roboto {}'.format(width//50))

#logo
logo = tkinter.PhotoImage(file='logo_kruh.png')
logo_b = tkinter.PhotoImage(file='logo.png')
logo_b = logo_b.subsample(2,2)
button = tkinter.Button(image=logo_b, command=zakladna, bg='white',activebackground='white',borderwidth=0)

# vseobecne buttony v menu
b1 = tkinter.Button(text='najviac predávaneé tovary', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat',activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: prva(b1))
b1.place(x=1, y=height//8*3, width=width//5)

b2 = tkinter.Button(text='najmenej predávané tovary', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: druha(b2))
b2.place(x=1, y=height//8*4, width=width//5)

b3 = tkinter.Button(text='priemerná cena nákupu', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: tretia(b3))
b3.place(x=1, y=height//8*5, width=width//5)

b4 = tkinter.Button(text='aktuálne tržby a náklady', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: stvrta(b4))
b4.place(x=1, y=height//8*6, width=width//5)
posledny_b = tkinter.Button() #na menenie farby buttonov v menu

#ine buttony
button_dnes = tkinter.Button(text='dnešné ceny nákupov', command=dnes, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)       
button_tyzden = tkinter.Button(text='týždňové ceny nákupov', command=tyzden, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)   
button4a = tkinter.Button(text='náklady a tržby', command=naklad_trzba, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)       
button4b = tkinter.Button(text='rozdiel nákladov a tržieb', command=rozdiel, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)
button_nepredane = tkinter.Button(text='tovary nepredané ani raz', command=nepredane, bg='#e0da63', relief='flat', height=3//2,
                                  activebackground='#aca932', borderwidth=0) 

#..............TAHANIE HODNOT Z TXT.....................

def nacitaj_statistiky():
    global nakup,predaj
    lock_s = open('STATISTIKY_LOCK.txt','w')
    lock_s.close()
    subor_s = open('STATISTIKY.txt', 'r', encoding='UTF-8')
    pocet_riadkov2 = subor_s.readline()
    predaj = []
    nakup = []
    for riadok in subor_s:
        riadok = riadok.strip().split(';')
        if riadok[0].upper() == 'P':
            predaj.append(riadok)
        elif riadok[0].upper() == 'N':
            nakup.append(riadok)
    subor_s.close()
    os.remove('STATISTIKY_LOCK.txt')
    upratanie_dat()
    
def statistiky_lock():
    if os.path.exists('STATISTIKY_LOCK.txt'):
        c.after(1000, nacitaj_statistiky)
    else:
        nacitaj_statistiky()

def tovar_lock():
    if os.path.exists('TOVAR_LOCK.txt'):
        c.after(1000,tovar_lock)
    else:
        nacitaj_tovar()

#priradenie nazvov
def nacitaj_tovar():
    global vobec_nepredane, najviac, najmenej
    lock_t = open('TOVAR_LOCK.txt','w')
    lock_t.close()
    subor_t = open('TOVAR.txt', 'r', encoding='UTF-8')
    pocet_riadkov1 = subor_t.readline()
    tovar = []
    for riadok in subor_t:
        riadok = riadok.strip().split(';')
        tovar.append(riadok)
    subor_t.close()
    os.remove('TOVAR_LOCK.txt')
    tovar = sorted(tovar)    
    vobec_nepredane = []
    a = 0
    b = 0
    for i in range(len(tovar)):
        pridaj = True
        if a < 10 and len(najviac) > a:
            if tovar[i][0] == najviac[a][0]:
                pom = tovar[i][1].replace(' ','\n')
                najviac[a][0] = pom
                a += 1
            elif tovar[i][0] > najviac[a][0]:
                a += 1
            else:
                vobec_nepredane.append(tovar[i][1])
                pridaj = False
        if b < 10 and len(najmenej) > b:
            if tovar[i][0] == najmenej[b][0]:
                pom = tovar[i][1].replace(' ','\n')
                najmenej[b][0] = pom
                b += 1
            elif tovar[i][0] > najmenej [b][0]:
                b += 1
            elif pridaj:
                vobec_nepredane.append(tovar[i][1])
    praca_s_datami()
    
def upratanie_dat():
    #treba spocitat, ak sa z jedneho kodu predalo viacero kusov v roznch nakupoch
    global najviac, najmenej
    kod_predanych = []
    pocet_predanych = []
    for prvok in predaj:
        if prvok[2] in kod_predanych:
            hladana = kod_predanych.index(prvok[2])
            pocet_predanych[hladana] = int(pocet_predanych[hladana])+int(prvok[3])
        else:
            kod_predanych.append(prvok[2])
            pocet_predanych.append(prvok[3])
    predane_tovary = list(zip(kod_predanych,pocet_predanych)) #vytvoreny zoznam s kodmi a poctami predanych

    #10 najpredavanejsich
    najviac = sorted(sorted(predane_tovary, reverse=True, key=lambda kluc: int(kluc[1]))[:10])#hladam 10 najviac
    najviac = list(map(list, najviac)) #musim prerobit n-tice v zozname na zoznamy
    #10 najmenej predavanych0
    najmenej = sorted(sorted(predane_tovary, key=lambda kluc: int(kluc[1]))[:10])
    najmenej = list(map(list, najmenej))

    tovar_lock()

def praca_s_datami():
    global hodnoty1, nazvy1, hodnoty2, nazvy2, najviac, najmenej, hod4trzby, hod4naklady, datumy, hodnoty3tyzden, hodnoty3den, dnesne_nakupy, casy
    najviac = sorted(najviac, reverse=True, key=lambda kluc: int(kluc[1]))#finalne zoradenie
    najmenej = sorted(najmenej, reverse=True, key=lambda kluc: int(kluc[1]))
    hodnoty1 = []
    nazvy1 = []
    hodnoty2 = []
    nazvy2 = []
    for i in range(10):
        if len(najviac) > i:
            hodnoty1.append(int(najviac[i][1]))
            nazvy1.append(najviac[i][0])
        if len(najmenej) > i and len(vobec_nepredane) > 10:
            hodnoty2.append(int(najmenej[i][1]))
            nazvy2.append(najmenej[i][0])
    if len(vobec_nepredane) < 10:
        for i in range(10-len(vobec_nepredane)):
            hodnoty2.append(int(najmenej[i][1]))
            nazvy2.append(najmenej[i][0])
        for i in range(len(vobec_nepredane)):
            hodnoty2.append(0)
            nazvy2.append(vobec_nepredane[i])
            
    #hodnoty dnesnych nakupov
    datum = time.strftime('%d.%m.%y', time.localtime())
    i = -1
    dnesne_nakupy = []
    casy = []
    while datum == predaj[i][6]:
        kus = int(predaj[i][3])
        cena = float(predaj[i][4])
        if i < -1 and predaj[i][1] == predaj[i+1][1]:
            stara_suma = dnesne_nakupy[-1]
            dnesne_nakupy[-1] = stara_suma + round(kus*cena,2)
        else:
            dnesne_nakupy.append(round(kus*cena,2))
            casy.append(predaj[i][5])
        i -= 1

    if dnesne_nakupy == []:
        dnesne_nakupy = [0.001]
    else:
        dnesne_nakupy.reverse()
    hodnoty3den = dnesne_nakupy
    casy.reverse()

    #priemerne hodnoty za tyzden a trzby
    posledny_datum = datetime.strftime(datetime.now() - timedelta(6), '%d.%m.%y')
    i = -1
    tyzden = []

    while i >= -len(predaj) and (posledny_datum <= predaj[i][6] or (posledny_datum[:2] >= predaj[i][6][:2]
                            and (posledny_datum[3:5] <= predaj[i][6][3:5] or (posledny_datum[3:5] == '12' and predaj[i][6][3:5] == '01')))):
        tyzden.append(predaj[i])
        i -= 1
        
    datumy = []
    trzby = [0 for i in range(7)]
    pocet = [0 for i in range(7)]
    for i in range(7):
        nasiel = False
        for j in range(len(tyzden)):
            if datetime.strftime(datetime.now() - timedelta(i), '%d.%m.%y') in tyzden[j]:
                transakcia = int(tyzden[j][1])
                index = j+1
                pocet[i] += 1
                trzby[i] += int(tyzden[j][3]) * float(tyzden[j][4])
                while index < len(tyzden) and datetime.strftime(datetime.now() - timedelta(i), '%d.%m.%y') in tyzden[index]:
                    trzby[i] += int(tyzden[index][3]) * float(tyzden[index][4])
                    if index < len(tyzden) and transakcia != int(tyzden[index][1]):
                        pocet[i] += 1
                        transakcia = int(tyzden[index][1])
                    index += 1
                datumy.append(datetime.strftime(datetime.now() - timedelta(i), '%d.%m.'))
                nasiel = True
                break
        if not nasiel:
            datumy.append(datetime.strftime(datetime.now() - timedelta(i), '%d.%m.'))
    hodnoty3tyzden = []
    for i in range(len(trzby)):
        if pocet[i] == 0:
            hodnoty3tyzden.append(0.001)
        else:
            hodnoty3tyzden.append(round(trzby[i]/pocet[i],2))
    datumy.reverse()
    hodnoty3tyzden.reverse()
    hod4trzby = []
    hod4trzby = trzby
    hod4trzby.reverse()

    #naklady
    i = -1
    tyzden2 = []
    while i > -len(nakup) and (posledny_datum <= nakup[i][6] or (posledny_datum[:2] >= nakup[i][6][:2]
                           and (posledny_datum[3:5] <= nakup[i][6][3:5] or (posledny_datum[3:5] == '12' and nakup[i][6][3:5] == '01')))):
        tyzden2.append(nakup[i])
        i -= 1
     
    naklady = [0 for i in range(7)]
    for i in range(7):
        nasiel = False
        for j in range(len(tyzden2)):
            if datetime.strftime(datetime.now() - timedelta(i), '%d.%m.%y') in tyzden2[j]:
                index = j+1
                naklady[i] += int(tyzden2[j][3]) * float(tyzden2[j][4])
                while index < len(tyzden2) and datetime.strftime(datetime.now() - timedelta(i), '%d.%m.%y') in tyzden2[index]:
                    naklady[i] += int(tyzden2[index][3]) * float(tyzden2[index][4])
                    index += 1
                datumy.append(datetime.strftime(datetime.now() - timedelta(i), '%d.%m.%y'))
                nasiel = True
                break
    naklady.reverse()
    hod4naklady = naklady

def aktualizacia():
    global aktual_obrazovka
    if cas_stat != os.path.getmtime('STATISTIKY.txt') or cas_tovar != os.path.getmtime('TOVAR.txt'):
        statistiky_lock()
        c.after(1000,aktualizacia)
        zakl_nast()
        if aktual_obrazovka == tretia or aktual_obrazovka == stvrta:
            aktual_graf()
        aktual_obrazovka(posledny_b)
            
    else:
        c.after(1000,aktualizacia)
        
#...............SPUSTANIE PROGRAMU......................
aktual_obrazovka = zakladna
aktual_graf = None
cas_stat = os.path.getmtime('STATISTIKY.txt')
cas_tovar = os.path.getmtime('TOVAR.txt')
statistiky_lock()
aktualizacia()
nakup = 1
ah = 1
mys = True
popis = c.create_text(0,0) # ku g3 - aby deletovalo, najprv musim vytvorit
cas = time.strftime('%A %d.%b %Y %H:%M:%S', time.localtime())
hodiny = c.create_text(width//15*14, height/30*29, text=cas)
spusti_cas()
zakladna(event = None)
