import tkinter
class TestiKeskiArvo:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()

        self.koe1_kehys = tkinter.Frame(self.paa_ikkuna)
        self.koe2_kehys = tkinter.Frame(self.paa_ikkuna)
        self.koe3_kehys = tkinter.Frame(self.paa_ikkuna)
        self.ka_kehys = tkinter.Frame(self.paa_ikkuna)
        self.painike_kehys = tkinter.Frame(self.paa_ikkuna)

        self.koe1_label = tkinter.Label(self.koe1_kehys, text="Koe1")
        self.koe1_syote = tkinter.Entry(self.koe1_kehys, width = 10)
        self.koe1_label.pack(side = 'left')
        self.koe1_syote.pack(side = 'left')

        self.koe2_label = tkinter.Label(self.koe2_kehys, text="Koe2")
        self.koe2_syote = tkinter.Entry(self.koe2_kehys, width = 10)
        self.koe2_label.pack(side = 'left')
        self.koe2_syote.pack(side = 'left')

        self.koe3_label = tkinter.Label(self.koe3_kehys, text="Koe3")
        self.koe3_syote = tkinter.Entry(self.koe3_kehys, width = 10)
        self.koe3_label.pack(side = 'left')
        self.koe3_syote.pack(side = 'left')

        self.tulos_label = tkinter.Label(self.ka_kehys, text = 'Keskiarvo:')
        self.tulos_label.pack(side = 'left')

        self.ka = tkinter.StringVar()
        self.ka_label = tkinter.Label(self.ka_kehys, textvariable = self.ka)
        self.ka_label.pack(side = 'left')

        self.laske_button = tkinter.Button(self.painike_kehys, text = 'Keskiarvo', command = self.laske_ka)
        self.lopeta_button = tkinter.Button(self.painike_kehys, text = 'Lopeta', command = self.paa_ikkuna.destroy)
        self.laske_button.pack(side = 'left')
        self.lopeta_button.pack(side = 'left')

        self.koe1_kehys.pack()
        self.koe2_kehys.pack()
        self.koe3_kehys.pack()
        self.ka_kehys.pack()
        self.painike_kehys.pack()

        tkinter.mainloop()
    def laske_ka(self):
            koe1 = float(self.koe1_syote.get())
            koe2 = float(self.koe2_syote.get())
            koe3 = float(self.koe3_syote.get())
            keskiarvo = round((koe1 + koe2 + koe3) / 3.0, 2)
            self.ka.set(keskiarvo)
testi_ka = TestiKeskiArvo()