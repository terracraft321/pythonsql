import tkinter
import tkinter.messagebox

class Matkamuunnin:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()

        self.yla_kehys = tkinter.Frame(self.paa_ikkuna)
        self.ala_kehys = tkinter.Frame(self.paa_ikkuna)

        self.kysy_teksti = tkinter.Label(self.yla_kehys, text="Anna matka kilometreinä")
        self.kilo_syote = tkinter.Entry(self.yla_kehys, width=10)

        self.kysy_teksti.pack(side='left')
        self.kilo_syote.pack(side='left')

        self.lasku_painike = tkinter.Button(self.ala_kehys, text='Muunna', command=self.muunna)
        self.lopetus_painike = tkinter.Button(self.ala_kehys, text='Lopeta', command=self.paa_ikkuna.destroy)

        self.lasku_painike.pack(side='left')
        self.lopetus_painike.pack(side='left')

        self.yla_kehys.pack()
        self.ala_kehys.pack()

        self.paa_ikkuna.mainloop()

    def muunna(self):
            kilo = float(self.kilo_syote.get())
            maili = kilo * 0.6214
            tkinter.messagebox.showinfo(' Tulokset ', str(kilo) + ' kilometria vastaa ' + str(maili) + ' mailia.')
kilo_muunnin = Matkamuunnin()
