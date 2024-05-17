import tkinter
import tkinter.messagebox

class OmaGUI:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()
        self.yla_kehys = tkinter.Frame(self.paa_ikkuna)
        self.ala_kehys = tkinter.Frame(self.paa_ikkuna)
        self.radio_muut = tkinter.IntVar()
        self.radio_muut.set(1)  # Corrected variable name

        self.rb1 = tkinter.Radiobutton(self.yla_kehys, text="Vaihtoehto 1", variable=self.radio_muut, value=1)
        self.rb2 = tkinter.Radiobutton(self.yla_kehys, text="Vaihtoehto 2", variable=self.radio_muut, value=2)
        self.rb3 = tkinter.Radiobutton(self.yla_kehys, text="Vaihtoehto 3", variable=self.radio_muut, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_painike = tkinter.Button(self.ala_kehys, text="OK", command=self.nayta_valinta)
        self.lopeta_painike = tkinter.Button(self.ala_kehys, text="Lopeta", command=self.paa_ikkuna.destroy)

        self.ok_painike.pack()
        self.lopeta_painike.pack()

        self.yla_kehys.pack()
        self.ala_kehys.pack()

        tkinter.mainloop()

    def nayta_valinta(self):
        tkinter.messagebox.showinfo('Valinta', 'Sinä valitsit ' + str(self.radio_muut.get()))

oma_gui = OmaGUI()
