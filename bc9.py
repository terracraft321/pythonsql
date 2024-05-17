import tkinter
import tkinter.messagebox


class MatkaMuunnin:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()

        self.yla_kehys = tkinter.Frame(self.paa_ikkuna)
        self.keski_kehys = tkinter.Frame(self.paa_ikkuna)
        self.ala_kehys = tkinter.Frame(self.paa_ikkuna)

        self.kysy_teksti = tkinter.Label(self.yla_kehys, text="Anna matka kilometreina:")
        self.kilo_syote = tkinter.Entry(self.yla_kehys, width=10)

        self.kysy_teksti.pack(side='left')
        self.kilo_syote.pack(side='left')

        self.selitys_teksti = tkinter.Label(self.keski_kehys, text='Muunnettava maileiksi:')
        self.arvo = tkinter.StringVar()
        self.mailit_teksti = tkinter.Label(self.keski_kehys, textvariable=self.arvo)
        self.selitys_teksti.pack(side='left')
        self.mailit_teksti.pack(side='left')

        self.lasku_painike = tkinter.Button(self.ala_kehys, text='Muunna', command=self.muunna)
        self.lopetus_painike = tkinter.Button(self.ala_kehys, text='Lopeta', command=self.paa_ikkuna.destroy)

        self.lasku_painike.pack(side='left')
        self.lopetus_painike.pack(side='left')

        self.yla_kehys.pack()
        self.keski_kehys.pack()
        self.ala_kehys.pack()

        tkinter.mainloop()

    def muunna(self):
        kilo = float(self.kilo_syote.get())
        maili = kilo * 0.6214
        self.arvo.set(maili)


kilo_muunnin = MatkaMuunnin()
