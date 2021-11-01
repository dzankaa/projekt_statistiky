import tkinter
import time

root = tkinter.Tk()
root.attributes('-fullscreen',True) # hlavne okno na celu obrazovku

c = tkinter.Canvas(root)
c.pack(fill=tkinter.BOTH, expand=True)

def zakl_nast():
    global w1_graf, w2_graf, h1_graf, h2_graf
    c.delete('text')
    tlacidlo()
    w1_graf = width//3
    w2_graf = width//4*3
    h1_graf = height//5*4
    h2_graf = height//7*2
    c.create_line(w1_graf, h1_graf , w2_graf, h1_graf, tags='menu') #vodorovna ciara grafu
    c.create_line(w1_graf, h1_graf , w1_graf, h2_graf, tags='menu') #zvisla ciara grafu

    
#definicie obrazoviek
def zakladna():
    c.delete('text')
    c.delete('menu')
    obrazok = c.create_image(width//5*3, height//2, image=logo, tags='text')
    
def prva():
    zakl_nast()
    c.create_text(width//2, height//6, text='NAJVIAC PREDAVANE TOVARY', font='Roboto 27', tags='text')
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
        
def druha():
    zakl_nast()
    c.create_text(width//2, height//6, text='NAJMENEJ PREDAVANE TOVARY', font='Roboto 27', tags='text')
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

def tretia():
    global pom_w3, pom_h3
    zakl_nast()
    c.bind('<Motion>', mys1)
    c.create_text(width//2, height//6, text='PRIEMERNA CENA NAKUPU', font='Roboto 27', tags='text')
    a = height//20
    c.create_text(width//8*7, height//3, text=' aktualna priemerna cena \n dnesnych nakupov: ', font='Roboto 15', tags='text')
    c.create_text(width//6*5, height//3+a, text=str(hodnoty3[6]), font='Roboto 15', tags='text')
    c.create_text(width//8*7, height//3+2*a, text='jednotlive ceny nakupov \n za posledny tyzden:', font='Roboto 15', tags='text')
    pom_w3 = (w2_graf - w1_graf)//len(hodnoty3)
    pom_h3 = (h1_graf - h2_graf)//max(hodnoty3)
    graf3 = ()
    for i in range(len(hodnoty3)):
        graf3 += (w1_graf+pom_w3*i+pom_w3//2, h1_graf-pom_h3*hodnoty3[i])
        c.create_oval(w1_graf+pom_w3*i+pom_w3//2-3, h1_graf-pom_h3*hodnoty3[i]-3, w1_graf+pom_w3*i+pom_w3//2+3, h1_graf-pom_h3*hodnoty3[i]+3, fill='#aca932', outline='#aca932', tags='text')
        c.create_text(width//6*5, height//3+2*(height//20)+a, text=str(hodnoty3[i]), font='Roboto 15', tags='text')
        a += height//20
    c.create_line(graf3, fill=('#aca932'), tags='text')
    c.create_text(width//2, h1_graf+(h1_graf-h2_graf)//15, text='priemerne hodnoty nakupov za posledny tyzden', font='Roboto 10', tags='text')
      
def stvrta():
    zakl_nast()
    c.create_text(width//2, height//6, text='AKTUALNE TRZBY A NAKLADY', font='Roboto 27', tags='text')
    c.create_text(width//8*7, height//2, text=' aktualna trzba: \n 812e \n aktualne naklady: \n 610e \n rozdiel: \n 202 \n', font='Roboto 20', tags='text')

def mys1(suradnice):
    xm = suradnice.x
    ym = suradnice.y
    for i in range(len(hodnoty3)):
        if (w1_graf+pom_w3*i+pom_w3//2-3 <= xm <= w1_graf+pom_w3*i+pom_w3//2+3) and (h1_graf-pom_h3*hodnoty3[i]-3 <= ym <= h1_graf-pom_h3*hodnoty3[i]+3):
            c.create_text(w1_graf+pom_w3*i+pom_w3//2-3, h1_graf-pom_h3*hodnoty3[i]-3, text=hodnoty3[i], font='Roboto 8', tags='okienko')
        
#na rusenie canvasu a velkost obrazovky
root.bind('<Escape>', lambda event: root.destroy())
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# nazov modulu a pozadia
c.create_rectangle(0, 0, width//4, height//7*2, fill='#679222', outline='#679222')
c.create_rectangle(width//4, 0, width, height, fill='lightgrey', outline='lightgrey')
c.create_rectangle(0, height//7*2, width//4, height, fill='whitesmoke', outline='whitesmoke')
c.create_line(width//4, height//15*14, width, height//15*14, fill='darkgrey', width=2)
c.create_line(width//4, 0, width//4, height, fill='darkgrey', width=2)
c.create_text(width//8, height//6, text='ŠTATISTIKY', font='Roboto 30')

# datum a cas
def spusti_cas():
    global hodiny
    c.delete(hodiny)
    cas = time.strftime('%A %d %B %Y %H:%M:%S', time.localtime())
    hodiny = c.create_text(width//9*8, height//60*59, text=cas)
    c.after(1000, spusti_cas)
    
cas = time.strftime('%A %d %B %Y %H:%M:%S', time.localtime())
hodiny = c.create_text(width//15*14, height//60*59, text=cas)
spusti_cas()

#logo
logo = tkinter.PhotoImage(file='logo.png')
photo = logo.subsample(2,2)
def tlacidlo():
    button = tkinter.Button(image=photo, command=zakladna, bg='lightgrey',
                            activebackground='lightgrey',borderwidth=0).place(x=width//5*4, y=height//10)
zakladna()

# buttony v menu
b1 = tkinter.Button(text='najviac predavane tovary',font='Roboto 15',width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=prva).place(x=width//25, y=height//8*3)
b2 = tkinter.Button(text='najmenej predavane tovary', font='Roboto 15',width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=druha).place(x=width//25, y=height//8*4)
b3 = tkinter.Button(text='priemerna cena nakupu', font='Roboto 15',width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=tretia).place(x=width//25, y=height//8*5)
b4 = tkinter.Button(text='aktualne trzby a naklady', font='Roboto 15',width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=stvrta).place(x=width//25, y=height//8*6)

# jednotlive hodnoty a nazvy ku grafom, ktore budu vytiahnute z textoveho suboru
hodnoty1 = [45,40,32,32,30,27,12,12,12,10]
nazvy1 = ['chlieb', 'jablko', 'zemiaky', 'mlieko', 'syr', 'muka', 'kava', 'tycinky', 'sunka', 'rozky']
hodnoty2 = [5,4,2,2,2,1,0,0,0,0]
nazvy2 = ['caj','marhule','sol','olej','kel','dzus','plienky','cukor','vajcia','mineralka']
hodnoty3 = [13,53,22,28,18,55,32]

