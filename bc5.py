import tkinter

class OmaGUI:
    def __init__(self):

        self.paa_ikkuna = tkinter.Tk()

        self.yla_kehys = tkinter.Frame(self.paa_ikkuna)
        self.ala_kehys = tkinter.Frame(self.paa_ikkuna)

        self.teksti1 = tkinter.Label(self.yla_kehys, text = "Vilkku")
        self.teksti2 = tkinter.Label(self.yla_kehys, text = 'Pilkku')
        self.teksti3 = tkinter.Label(self.yla_kehys, text = 'Tilkku')

        self.teksti1.pack(side = 'top')
        self.teksti2.pack(side = 'top')
        self.teksti3.pack(side = 'top')

        self.teksti4 = tkinter.Label(self.ala_kehys, text = "Vilkku")
        self.teksti5 = tkinter.Label(self.ala_kehys, text = 'Pilkku')
        self.teksti6 = tkinter.Label(self.ala_kehys, text = 'Tilkku')

        self.teksti4.pack(side = 'left')
        self.teksti5.pack(side = 'left')
        self.teksti6.pack(side = 'left')

        self.yla_kehys.pack()
        self.ala_kehys.pack()

        tkinter.mainloop()
oma_gui = OmaGUI()