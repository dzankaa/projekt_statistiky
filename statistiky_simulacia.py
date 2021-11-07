import tkinter
import time

root = tkinter.Tk()
root.attributes('-fullscreen',True) # hlavne okno na celu obrazovku

c = tkinter.Canvas(root)
c.pack(fill=tkinter.BOTH, expand=True)

#na rusenie canvasu a velkost obrazovky
root.bind('<Escape>', lambda event: root.destroy())
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

def zakl_nast():
    global w1_graf, w2_graf, h1_graf, h2_graf, ciara1, ciara2
    c.delete('text', 'g3')
    button.place(x=width//5*4, y=height//10)
    w1_graf = width//3
    w2_graf = width//4*3
    h1_graf = height//5*4
    h2_graf = height//7*2
    ciara1 = c.create_line(w1_graf, h1_graf , w2_graf, h1_graf, tags='menu') #vodorovna ciara grafu
    ciara2 = c.create_line(w1_graf, h1_graf , w1_graf, h2_graf, tags='menu') #zvisla ciara grafu
    button_tyzden.place(x=-1000, y=0)
    button_dnes.place(x=-1000, y=0)
    button4a.place(x=-1000, y=0)
    button4b.place(x=-1000, y=0) 

#definicie obrazoviek
def zakladna():
    c.delete('text', 'menu', 'g3')
    button.place(x=-1000, y=-1000)
    obrazok = c.create_image(width//5*3, height//2, image=logo, tags='text')
    button_tyzden.place(x=-1000, y=0)
    button_dnes.place(x=-1000, y=0) 
    
def prva(b1):
    global posledny_b
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b1['bg']=b1['activebackground']='#679222'
    posledny_b=b1
    zakl_nast()
    c.create_text(width//5*2, height//6, text='NAJVIAC PREDAVANE TOVARY', font='Roboto 27', tags='text')
    pom_w = (w2_graf - w1_graf)//len(hodnoty1)
    pom_h = (h1_graf - h2_graf)//hodnoty1[0]
    a = 0
    for i in range(len(hodnoty1)):
        c.create_rectangle(w1_graf+pom_w*i+pom_w//6, h1_graf, w1_graf+pom_w*i+pom_w-pom_w//6, h1_graf-pom_h*hodnoty1[i],fill=('#e0da63'), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf-pom_h*int(hodnoty1[i])-(h1_graf-h2_graf)//15, text=str(hodnoty1[i]), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf+(h1_graf-h2_graf)//15, text=nazvy1[i], tags='text')
        c.create_text(width//6*5, height//3+a, text=nazvy1[i], font='Roboto 15', tags='text')
        c.create_text(width//8*7, height//3+a, text=str(hodnoty1[i]), font='Roboto 15', tags='text')
        a += height//20
        
def druha(b2):
    global posledny_b
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b2['bg']=b2['activebackground']='#679222'
    posledny_b=b2
    zakl_nast()
    c.create_text(width//5*2, height//6, text='NAJMENEJ PREDAVANE TOVARY', font='Roboto 27', tags='text')
    pom_w = (w2_graf - w1_graf)//len(hodnoty2)
    pom_h = (h1_graf - h2_graf)//hodnoty2[0]
    a = 0
    for i in range(len(hodnoty2)):
        c.create_rectangle(w1_graf+pom_w*i+pom_w//6, h1_graf, w1_graf+pom_w*i+pom_w-pom_w//6, h1_graf-pom_h*hodnoty2[i],fill=('#e0da63'), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf-pom_h*int(hodnoty2[i])-(h1_graf-h2_graf)//15, text=str(hodnoty2[i]), tags='text')
        c.create_text(w1_graf+pom_w*i+pom_w//2, h1_graf+(h1_graf-h2_graf)//15, text=nazvy2[i], tags='text')
        c.create_text(width//6*5, height//3+a, text=nazvy2[i], font='Roboto 15', tags='text')
        c.create_text(width//8*7, height//3+a, text=str(hodnoty2[i]), font='Roboto 15', tags='text')
        a += height//20

def tretia(b3):
    global pom_w3, pom_h3, hod3, nakup, posledny_b
    posledny_b['bg']=posledny_b['activebackground']='#98c151'
    b3['bg']=b3['activebackground']='#679222'
    posledny_b=b3
    c.delete('g3')
    zakl_nast()
    button_dnes.place(x=width//9*2, y=height//8*7)
    button_tyzden.place(x=width//9*2, y=height//6*5) 
    c.bind('<Motion>', mys1)
    c.create_text(width//5*2, height//6, text='PRIEMERNA CENA NAKUPU', font='Roboto 27', tags='text')
    a = height//20
    c.create_text(width//8*7, height//3, text=' aktualna priemerna cena \n dnesnych nakupov: ', font='Roboto 15', tags='text')
    c.create_text(width//6*5, height//3+a, text=str(hodnoty3tyzden[6]), font='Roboto 15', tags='text')
    c.create_text(width//8*7, height//3+2*a, text='priemerne ceny nakupov \n za posledny tyzden:', font='Roboto 15', tags='text')
    if nakup:
        hod3 = hodnoty3den
        dopln = 'dnesny den'        
    else:
        hod3 = hodnoty3tyzden
        dopln = 'posledny tyzden'
    pom_w3 = (w2_graf - w1_graf)//len(hod3)
    pom_h3 = (h1_graf - h2_graf)//max(hod3)
    graf3 = ()
    cisla=20
    
    for i in range(max(hod3)//20):
        c.create_oval(w1_graf-3, h1_graf-((h1_graf-h2_graf)//max(hod3))*cisla-3,w1_graf+3, h1_graf-((h1_graf-h2_graf)//max(hod3))*cisla+3, fill='black', tags='g3')
        c.create_text(w1_graf-width//100, h1_graf-((h1_graf-h2_graf)//max(hod3))*cisla, text=str(cisla), tags='g3')
        cisla += 20
    for i in range(len(hod3)):
        graf3 += (w1_graf+pom_w3*i+pom_w3//2, h1_graf-pom_h3*hod3[i])
        c.create_oval(w1_graf+pom_w3*i+pom_w3//2-3, h1_graf-pom_h3*hod3[i]-3, w1_graf+pom_w3*i+pom_w3//2+3, h1_graf-pom_h3*hod3[i]+3, fill='#aca932', outline='#aca932',tags='g3')
        c.create_text(width//6*5, height//3+2*(height//20)+a, text=str(hodnoty3tyzden[i]), font='Roboto 15', tags='g3')
        a += height//20
    c.create_line(graf3, fill=('#aca932'), tags='g3') 
    c.create_text(width//2, h1_graf+(h1_graf-h2_graf)//15, text='priemerne hodnoty nakupov za '+dopln, font='Roboto 10', tags='text')
      
def stvrta(b4):
    global posledny_b, ciara1,ciara2
    posledny_b['bg']='#98c151'
    b4['bg']='#679222'
    posledny_b=b4 
    zakl_nast()
    c.delete(ciara1,ciara2)
    button4a.place(x=width//9*2, y=height//8*7)
    button4b.place(x=width//9*2, y=height//6*5)
    naklad_trzba()
    c.create_text(width//5*2, height//6, text='AKTUALNE TRZBY A NAKLADY', font='Roboto 27', tags='text')
    c.create_text(width//8*7, height//2, text=' aktualna trzba: \n 812e \n aktualne naklady: \n 610e \n rozdiel: \n 202 \n', font='Roboto 15', tags='text')
    
    
# definicie ku stvtej obrazovke

def naklad_trzba():
    c.create_image(width//9*5, height//7*4, image=g4a, tags='text')

def rozdiel():
    c.create_image(width//9*5, height//7*4, image=g4b, tags='text')

button4a = tkinter.Button(text='naklady a trzby', command=naklad_trzba, bg='#e0da63', relief='flat', height=3//2, width=width//70,
                             activebackground='#aca932', borderwidth=0)       
button4b = tkinter.Button(text='rozdiel nakupu a trzieb', command=rozdiel, bg='#e0da63', relief='flat', height=3//2, width=width//70,
                             activebackground='#aca932', borderwidth=0)       
    
# definicie k tretej obrazovke
def mys1(suradnice):
    xm = suradnice.x
    ym = suradnice.y
    global popis
    c.delete(popis)
    for i in range(len(hod3)):
        if (w1_graf+pom_w3*i+pom_w3//2-10 <= xm <= w1_graf+pom_w3*i+pom_w3//2+10) and (h1_graf-pom_h3*hod3[i]-10 <= ym <= h1_graf-pom_h3*hod3[i]+10):
            popis = c.create_text(w1_graf+pom_w3*i+pom_w3//2-3, h1_graf-pom_h3*hod3[i]-3, text=hod3[i], font='Roboto 8', tags='g3')
            break       
def dnes():
    global nakup
    nakup = 1
    tretia(b3)

def tyzden():
    global nakup
    nakup = 0
    tretia(b3)
nakup=1
button_dnes = tkinter.Button(text='dnesne ceny nakupov', command=dnes, bg='#e0da63', relief='flat', height=3//2, width=width//70,
                             activebackground='#aca932', borderwidth=0)       
button_tyzden = tkinter.Button(text='tyzdnove ceny nakupov', command=tyzden, bg='#e0da63', relief='flat', height=3//2, width=width//70,
                             activebackground='#aca932', borderwidth=0)       

# nazov modulu a pozadia
c.create_rectangle(width//5, 0, width, height, fill='lightgrey', outline='lightgrey')
c.create_rectangle(0, 0, width//5, height, fill='#98c151', outline='#98c151')
c.create_line(width//5, height//15*14, width, height//15*14, fill='darkgrey', width=2)
c.create_line(width//5, 0, width//5, height, fill='darkgrey', width=2)
c.create_text(width//10, height//6, text='ŠTATISTIKY', font='Roboto {}'.format(width//50), fill='white')

# datum a cas
def spusti_cas():
    global hodiny
    c.delete(hodiny)
    cas = time.strftime('%A %d.%b %Y %H:%M:%S', time.localtime())
    hodiny = c.create_text(width//9*8, height//60*59, text=cas)
    c.after(1000, spusti_cas) 
cas = time.strftime('%A %d.%b %Y %H:%M:%S', time.localtime())
hodiny = c.create_text(width//15*14, height//60*59, text=cas)
spusti_cas()

#logo
logo = tkinter.PhotoImage(file='logo.png')
photo = logo.subsample(2,2)
button = tkinter.Button(image=photo, command=zakladna, bg='lightgrey',activebackground='lightgrey',borderwidth=0)

zakladna()

# vseobecne buttony v menu
b1 = tkinter.Button(text='najviac predavane tovary', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', width=width//56, bg='#98c151',
                    relief='flat',activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: prva(b1))
b1.place(x=2, y=height//8*3)

b2 = tkinter.Button(text='najmenej predavane tovary', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', width=width//56, bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: druha(b2))
b2.place(x=2, y=height//8*4)

b3 = tkinter.Button(text='priemerna cena nakupu', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', width=width//56, bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: tretia(b3))
b3.place(x=2, y=height//8*5)

b4 = tkinter.Button(text='aktualne trzby a naklady', font='Roboto {}'.format(width//100), fg="white", activeforeground='white', width=width//56, bg='#98c151',
                    relief='flat', activebackground='#679222', anchor='w', height=2, borderwidth=0, command=lambda: stvrta(b4))
b4.place(x=2, y=height//8*6)

# jednotlive hodnoty a nazvy ku grafom, ktore budu vytiahnute z textoveho suboru
hodnoty1 = [45,40,32,32,30,27,12,12,12,10]
nazvy1 = ['chlieb', 'jablko', 'zemiaky', 'mlieko', 'syr', 'muka', 'kava', 'tycinky', 'sunka', 'rozky']
hodnoty2 = [5,4,2,2,2,1,0,0,0,0]
nazvy2 = ['caj','marhule','sol','olej','kel','dzus','plienky','cukor','vajcia','mineralka']
hodnoty3tyzden = [13,53,22,80,180,55,32]
hodnoty3den = [31,30,14,25,50,39]

# ku grafu 3 - aby mohlo deletovat, najprv to musim vytvorit
popis = c.create_text(0,0)

posledny_b = tkinter.Button()

g4a = tkinter.PhotoImage(file='graf4a.png')
g4b = tkinter.PhotoImage(file='graf4b.png')

