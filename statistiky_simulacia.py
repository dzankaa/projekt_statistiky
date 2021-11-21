import tkinter
import time
from datetime import datetime, timedelta

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
def zakladna():
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
    global posledny_b
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b1['bg']=b1['activebackground']='#679222'
    posledny_b=b1
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
    global posledny_b
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b2['bg']=b2['activebackground']='#679222'
    posledny_b=b2
    zakl_nast()
    c.create_text(width//5*2, height//6, text='Najmenej predávané tovary', font='Roboto 27', tags='text')
    if max(hodnoty2) == 0:
        pom_h = 0
        c.create_text(width/5*2, height/2, text='tieto polozky \nsa nepredali \nani raz', font='Roboto 15', fill='#e0da63', tags='text')
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
    if len(vobec_nepredane) > 0:
            button_nepredane.place(x=width//9*2, y=height//8*7, width=width/10)

def nepredane():
    okno = tkinter.Toplevel(root)
    okno.lift()
    okno.title('Nepredane tovary')
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
    global pom_w3, pom_h3, hod3, nakup, posledny_b, mys, pom
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b3['bg']=b3['activebackground']='#679222'
    posledny_b=b3
    c.delete('g3')
    zakl_nast()
    button_tyzden.place(x=width//9*2, y=height//8*7, width=width//10)
    button_dnes.place(x=width//9*2, y=height//6*5, width=width//10)
    mys = True
    pom = 3
    c.bind('<Motion>', myska)
    c.create_text(width//5*2, height//6, text='Priemerná cena nákupu', font='Roboto 27', tags='text')
    a = height//20
    c.create_text(width//8*7, height//3, text=' aktualna priemerna cena \n dnesnych nakupov: ', font='Roboto 12', tags='text')
    c.create_text(width//9*8, height//3+a, text=str(hodnoty3tyzden[-1]), font='Roboto 11', tags='text')
    c.create_text(width//8*7, height//3+2*a, text='priemerne ceny nakupov \n za posledny tyzden:', font='Roboto 12', tags='text')
    if nakup:
        hod3 = hodnoty3den
        dopln = 'dnesny den'
        button_dnes['bg']=button_dnes['activebackground']='#aca932'
        button_tyzden['bg']=button_tyzden['activebackground']='#e0da63'
    else:
        hod3 = hodnoty3tyzden
        dopln = 'posledny tyzden'
        button_tyzden['bg']=button_tyzden['activebackground']='#aca932'
        button_dnes['bg']=button_dnes['activebackground']='#e0da63'
    pom_w3 = (w2_graf - w1_graf)/len(hod3)
    pom_h3 = (h1_graf - h2_graf)/max(hod3)
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
    for i in range(len(hodnoty3tyzden)):
        c.create_text(width//9*8, height//3+2*(height//20)+a, text=str(hodnoty3tyzden[i]), font='Roboto 11', tags='g3')
        c.create_text(width//7*6, height//3+2*(height//20)+a, text=str(datumy[i]), font='Roboto 11', tags='g3')
        a += height/20
    c.create_line(graf3, fill='#aca932', tags='g3') 
    c.create_text(width/2, h1_graf+h1_graf/20, text='hodnoty nakupov za '+dopln, font='Roboto 15', tags='text')
    c.create_text(width/2, h1_graf+h1_graf/10, text='pre zobrazenie konkrétnych hodnôt prejdi myšou cez body', font='Roboto 10', tags='text')
      
def stvrta(b4):
    global posledny_b
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b4['bg']=b4['activebackground']='#679222'
    posledny_b=b4
    zakl_nast()
    mys = True
    button4b.place(x=width//9*2, y=height//8*7, width=width/10)
    button4a.place(x=width//9*2, y=height//6*5, width=width/10)
    naklad_trzba()
    c.create_text(width//5*2, height//6, text='Aktuálne tržby a náklady', font='Roboto 27', tags='text')
    c.create_text(width/2, h1_graf+h1_graf/20, text='pre zobrazenie konkrétnych hodnôt prejdi myšou cez body', font='Roboto 10', tags='text')
    hod4 = ['aktuálna tržba:', str(hod4trzby[-1]), 'aktuálne náklady:', str(hod4naklady[-1]), 'rozdiel:', str(hod4trzby[-1]-hod4naklady[-1])]
    a = height/20
    for i in range(6):
        c.create_text(width/7*6, height/5*2+a*i, text=hod4[i], font='Roboto 11', tags='text')

# definicie ku stvtej obrazovke
def naklad_trzba():
    global ciara1,pom,mys,pom_w4,pom_h4
    c.delete('g4c')
    button4a['bg']=button_dnes['activebackground']='#aca932'
    button4b['bg']=button_tyzden['activebackground']='#e0da63'
    graf4a = ()
    graf4b = ()
    maxi = max(hod4trzby+hod4naklady)
    pom_h4 = (h1_graf - h2_graf)/maxi
    pom_w4 = (w2_graf - w1_graf)/len(hod4trzby)
    c.create_line(w1_graf, h1_graf , w2_graf, h1_graf, tags='g4ab')
    cisla = maxi/5
    for i in range(5):
        c.create_oval(w1_graf-3, h1_graf-((h1_graf-h2_graf)/maxi)*cisla-3,w1_graf+3, h1_graf-((h1_graf-h2_graf)/maxi)*cisla+3, fill='black', tags='g4ab')
        c.create_text(w1_graf-width//80, h1_graf-((h1_graf-h2_graf)/maxi)*cisla, text=str(cisla), tags='g4ab')
        cisla += maxi/5
    for i in range(len(hod4trzby)):
        graf4a += (w1_graf+pom_w4*i+pom_w4//2, h1_graf-(pom_h4*hod4trzby[i]))
        graf4b += (w1_graf+pom_w4*i+pom_w4//2, h1_graf-(pom_h4*hod4naklady[i]))
        c.create_oval(w1_graf+pom_w4*i+pom_w4//2-3, h1_graf-pom_h4*hod4trzby[i]-3, w1_graf+pom_w4*i+pom_w4//2+3, h1_graf-pom_h4*hod4trzby[i]+3, fill='#679222', outline='#679222',tags='g4ab')
        c.create_oval(w1_graf+pom_w4*i+pom_w4//2-3, h1_graf-pom_h4*hod4naklady[i]-3, w1_graf+pom_w4*i+pom_w4//2+3, h1_graf-pom_h4*hod4naklady[i]+3, fill='#aca932', outline='#aca932',tags='g4ab')
    c.create_line(graf4a, fill='#679222', tags='g4ab')
    c.create_line(graf4b, fill='#aca932', tags='g4ab')
    c.create_text(w2_graf-w2_graf/12, h1_graf+h1_graf/20, text='tržby', font='Roboto 10', tags='g4ab')
    c.create_text(w2_graf-w2_graf/12, h1_graf+h1_graf/10, text='náklady', font='Roboto 10', tags='g4ab')
    c.create_line(w2_graf, h1_graf+h1_graf/20, w2_graf-w2_graf/20 ,h1_graf+h1_graf/20, fill='#679222', width=3, tags='g4ab')
    c.create_line(w2_graf, h1_graf+h1_graf/10, w2_graf-w2_graf/20 ,h1_graf+h1_graf/10, fill='#aca932', width=3, tags='g4ab')
    mys = True
    pom = 4
    c.bind('<Motion>', myska)
    
def rozdiel():
    global pom,mys,hod4roz,h4_graf,dielik
    c.delete('g4ab', 'menu2')
    button4b['bg']=button_dnes['activebackground']='#aca932'
    button4a['bg']=button_tyzden['activebackground']='#e0da63'
    hod4roz = ()
    for i in range(len(hod4trzby)):
        hod4roz += (round(hod4trzby[i]-hod4naklady[i],2),)
    maxi = max(hod4roz)
    mini = min(hod4roz)
    dielik = (h1_graf - h2_graf)/(abs(maxi)+abs(mini))
    h4_graf = h1_graf-(abs(mini)*dielik)
    c.create_line(w1_graf, h4_graf , w2_graf, h4_graf, tags='g4c')
    pom_w4 = (w2_graf - w1_graf)/len(hod4trzby)
    graf4c = ()
    cisla = round(mini/10)*10
    for i in range(6):
        c.create_oval(w1_graf-3, h4_graf-dielik*cisla-3, w1_graf+3, h4_graf-dielik*cisla+3, fill='black', tags='g4c')
        c.create_text(w1_graf-width//80, h4_graf-dielik*cisla, text=str(cisla), tags='g4c')
        cisla += round(((abs(mini)+abs(maxi))/6)/10)*10
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
                    pomocna = '\ncas: '+casy[i]
                else:
                    pomocna = '\ndatum: '+datumy[i]
                popis = c.create_text(w1_graf+pom_w3*i+pom_w3//2-10, h1_graf-pom_h3*hod3[i]-20, text='hodnota: '+str(hod3[i])+pomocna, font='Roboto 8', tags='g3')
                
    elif pom == 4:
        for i in range(len(hod4trzby)):
            if (w1_graf+pom_w4*i+pom_w4//2-10 <= xm <= w1_graf+pom_w4*i+pom_w4//2+10) and (h1_graf-pom_h4*hod4trzby[i]-10 <= ym <= h1_graf-pom_h4*hod4trzby[i]+10):
                popis = c.create_text(w1_graf+pom_w4*i+pom_w4//2-10, h1_graf-pom_h4*hod4trzby[i]-20, text='hodnota: '+str(hod4trzby[i])+'\ndatum: '+datumy[i], font='Roboto 8', tags='g4ab')
                
            elif (w1_graf+pom_w4*i+pom_w4//2-10 <= xm <= w1_graf+pom_w4*i+pom_w4//2+10) and (h1_graf-pom_h4*hod4naklady[i]-10 <= ym <= h1_graf-pom_h4*hod4naklady[i]+10):
                popis = c.create_text(w1_graf+pom_w4*i+pom_w4//2-10, h1_graf-pom_h4*hod4naklady[i]-20, text='hodnota: '+str(hod4naklady[i])+'\ndatum: '+datumy[i], font='Roboto 8', tags='g4ab')
    if pom == 5:
        for i in range(len(hod4roz)):
            if (w1_graf+pom_w4*i+pom_w4//2-10 <= xm <= w1_graf+pom_w4*i+pom_w4//2+10) and (h4_graf-dielik*hod4roz[i]-10 <= ym <= h4_graf-dielik*hod4roz[i]+10):
                popis = c.create_text(w1_graf+pom_w4*i+pom_w4//2-10, h4_graf-dielik*hod4roz[i]-20, text='hodnota: '+str(hod4roz[i])+'\ndatum: '+datumy[i], font='Roboto 8', tags='g4c')                
                                              
def dnes():
    global nakup
    nakup = 1
    tretia(b3)

def tyzden():
    global nakup
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
b1 = tkinter.Button(text='najviac predavane tovary', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat',activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: prva(b1))
b1.place(x=1, y=height//8*3, width=width//5)

b2 = tkinter.Button(text='najmenej predavane tovary', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: druha(b2))
b2.place(x=1, y=height//8*4, width=width//5)

b3 = tkinter.Button(text='priemerna cena nakupu', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: tretia(b3))
b3.place(x=1, y=height//8*5, width=width//5)

b4 = tkinter.Button(text='aktualne trzby a naklady', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: stvrta(b4))
b4.place(x=1, y=height//8*6, width=width//5)
posledny_b = tkinter.Button() #na menenie farby buttonov v menu

#ine buttony
button_dnes = tkinter.Button(text='dnesne ceny nakupov', command=dnes, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)       
button_tyzden = tkinter.Button(text='tyzdnove ceny nakupov', command=tyzden, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)   
button4a = tkinter.Button(text='naklady a trzby', command=naklad_trzba, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)       
button4b = tkinter.Button(text='rozdiel nakupu a trzieb', command=rozdiel, bg='#e0da63', relief='flat', height=3//2,
                             activebackground='#aca932', borderwidth=0)
button_nepredane = tkinter.Button(text='tovary nepredane ani raz', command=nepredane, bg='#e0da63', relief='flat', height=3//2,
                                  activebackground='#aca932', borderwidth=0) 

#..............TAHANIE HODNOT Z TXT.....................
subor_s = open('STATISTIKY.txt', 'r', encoding='UTF-8')
pocet_riadkov2 = subor_s.readline()

predaj = []
nakup = []
for riadok in subor_s:
    riadok = riadok.strip().split(';')
    if riadok[0].upper() == 'P':
        predaj.append(riadok)
    else:
        nakup.append(riadok)
subor_s.close()
#treba spocitat, ak sa z jedneho kodu predalo viacero kusov v roznch nakupoch
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

#priradenie nazvov
subor_t = open('TOVAR.txt', 'r', encoding='UTF-8')
pocet_riadkov1 = subor_t.readline()
vobec_nepredane = []
a = 0
b = 0
for i in range(int(pocet_riadkov1)-1):
    riadok = subor_t.readline().strip()
    if a < 10 and riadok[:4] == najviac[a][0] :
        pom = riadok[5:].replace(' ','\n')
        najviac[a][0] = pom
        a += 1
    if b < 10 and riadok[:4] == najmenej[b][0]:
        pom = riadok[5:].replace(' ','\n')
        najmenej[b][0] = pom
        b += 1
    else:
        vobec_nepredane.append(riadok[5:])
        pridaj = False
subor_t.close()
najviac = sorted(najviac, reverse=True, key=lambda kluc: int(kluc[1]))#finalne zoradenie
najmenej = sorted(najmenej, reverse=True, key=lambda kluc: int(kluc[1]))
hodnoty1 = []
nazvy1 = []
hodnoty2 = []
nazvy2 = []
for i in range(10):
    hodnoty1.append(int(najviac[i][1]))
    nazvy1.append(najviac[i][0])
    hodnoty2.append(int(najmenej[i][1]))
    nazvy2.append(najmenej[i][0])

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
dnesne_nakupy.reverse()
if dnesne_nakupy == []:
    dnesne_nakupy = [0]
hodnoty3den = dnesne_nakupy
casy.reverse()

#priemerne hodnoty za tyzden a trzby
posledny_datum = datetime.strftime(datetime.now() - timedelta(6), '%d.%m.%y')
i = -1
pocet = 1
trzby = []
pocet = []
datumy = []
while i > -len(predaj) or posledny_datum[:2] <= predaj[i][6][:2]: 
    kus = int(predaj[i][3])
    cena = float(predaj[i][4])
    if i < -1 and predaj[i][6] == predaj[i+1][6]:
        stara_suma = trzby[-1]
        trzby[-1] = round(stara_suma + kus*cena,2)
        stary_pocet = pocet[-1]
        pocet[-1] = stary_pocet+1
    else:
        trzby.append(round(kus*cena,2))
        pocet.append(1)
        datumy.append(predaj[i][6][:6])
    i -= 1
trzby.reverse()
hod4trzby = trzby
tyzdnovy_nakup = [round(i/j,2) for i,j in zip(trzby, pocet)]
hodnoty3tyzden = tyzdnovy_nakup
datumy.reverse()

#naklady
i = -1
naklady = []
while i > -len(nakup) or posledny_datum[:2] <= nakup[i][6][:2]: 
    kus = int(nakup[i][3])
    cena = float(nakup[i][4])
    if i < -1 and nakup[i][6] == nakup[i+1][6]:
        stara_suma = naklady[-1]
        naklady[-1] = round(stara_suma + kus*cena,2)
    else:
        naklady.append(round(kus*cena,2))
    i -= 1
naklady.reverse()
hod4naklady = naklady



#...............SPUSTANIE PROGRAMU......................
nakup=1
mys = True
popis = c.create_text(0,0) # ku g3 - aby deletovalo, najprv musim vytvorit
cas = time.strftime('%A %d.%b %Y %H:%M:%S', time.localtime())
hodiny = c.create_text(width//15*14, height/30*29, text=cas)
spusti_cas()
zakladna()
