import tkinter

root = tkinter.Tk()
root.attributes('-fullscreen',True) # hlavne okno na celu obrazovku

c = tkinter.Canvas(root)
c.pack(fill=tkinter.BOTH, expand=True)

#definicie obrazoviek
def prva():
    c.delete('text')
    c.coords(obrazok, width//8*7, height//6)
    c.create_text(width//8*4, height//6, text='NAJVIAC PREDAVANE TOVARY', font='Roboto 27', tags='text')
    c.create_image(width//2, height//5*3, image=g1, tags='text')
    c.create_text(width//8*7, height//2, text=' chlieb - 45 \n jablka - 40 \n zemiaky - 37 \n mlieko - 35 \n syr - 32 \n muka - 20 \n kava - 20 \n tycinky - 15 \n sunka - 13 \n rozky - 11', font='Roboto 20', tags='text')

def druha():
    c.delete('text')
    c.coords(obrazok, width//8*7, height//6)
    c.create_text(width//8*4, height//6, text='NAJMENEJ PREDAVANE TOVARY', font='Roboto 27', tags='text')
    c.create_image(width//2, height//5*3, image=g2, tags='text')
    c.create_text(width//8*7, height//2, text=' caj - 5 \n marhule - 4 \n sol - 3 \n olej - 3 \n kel - 2 \n dzus - 1 \n plienky - 1 \n cukor - / \n vajcia - / \n mineralka - /', font='Roboto 20', tags='text')

def tretia():
    c.delete('text')
    c.coords(obrazok, width//8*7, height//6)
    c.create_text(width//8*4, height//6, text='PRIEMERNA CENA NAKUPU', font='Roboto 27', tags='text')
    c.create_image(width//2, height//5*3, image=g3, tags='text')
    c.create_text(width//8*7, height//2, text=' priemerna cena: 32 \n jednotlive ceny: \n 13 \n 53 \n 22 \n 28 \n 18 \n 55 \n 32 ', font='Roboto 20', tags='text')

def stvrta():
    c.delete('text')
    c.coords(obrazok, width//8*7, height//6)
    c.create_text(width//8*4, height//6, text='AKTUALNE TRZBY A NAKLADY', font='Roboto 27', tags='text')
    c.create_image(width//2, height//5*3, image=g4, tags='text')
    c.create_text(width//8*7, height//2, text=' aktualna trzba: \n 812e \n aktualne naklady: \n 610e \n rozdiel: \n 202 \n', font='Roboto 20', tags='text')

    
#na rusenie canvasu a velkost obrazovky
root.bind('<Escape>', lambda event: root.destroy())
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# nazov modulu a pozadia
c.create_rectangle(0, 0, width//4, height//7*2, fill='#679222', outline='#679222')
c.create_rectangle(width//4, 0, width, height, fill='lightgrey', outline='lightgrey')
c.create_rectangle(0, height//7*2, width//4, height, fill='white', outline='white')
c.create_text(width//8, height//6, text='ŠTATISTIKY', font='Roboto 30' )

#logo
logo = tkinter.PhotoImage(file='LOGO_hypermarket.png')
obrazok = c.create_image(width//5*3, height//2, image=logo)

# buttony v menu
b1 = tkinter.Button(text='najviac predavane tovary',font='Roboto 15',
                    width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=prva).place(x=width//25, y=height//8*3)
b2 = tkinter.Button(text='najmenej predavane tovary', font='Roboto 15',
                    width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=druha).place(x=width//25, y=height//8*4)
b3 = tkinter.Button(text='priemerna cena nakupu', font='Roboto 15',
                    width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=tretia).place(x=width//25, y=height//8*5)
b4 = tkinter.Button(text='aktualne trzby a naklady', font='Roboto 15',
                    width=width//65, bg='#98c151',
                    relief='raised', bd=3, activebackground='#98c151', command=stvrta).place(x=width//25, y=height//8*6)

g1 = tkinter.PhotoImage(file='graf1.png')
g2 = tkinter.PhotoImage(file='graf2.png')
g3 = tkinter.PhotoImage(file='graf3.png')
g4 = tkinter.PhotoImage(file='graf4.png')
