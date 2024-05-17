import tkinter
import tkinter.messagebox


class OmaGUI:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()
        self.yla_kehys = tkinter.Frame(self.paa_ikkuna)
        self.ala_kehys = tkinter.Frame(self.paa_ikkuna)
        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.yla_kehys, text="Vaihtoehto 1", variable=self.var1)
        self.cb2 = tkinter.Checkbutton(self.yla_kehys, text="Vaihtoehto 2", variable=self.var2)
        self.cb3 = tkinter.Checkbutton(self.yla_kehys, text="Vaihtoehto 3", variable=self.var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.ok_painike = tkinter.Button(self.ala_kehys, text="OK", command=self.nayta_valinta)
        self.lopeta_painike = tkinter.Button(self.ala_kehys, text="Lopeta", command=self.paa_ikkuna.destroy)

        self.ok_painike.pack()
        self.lopeta_painike.pack()

        self.yla_kehys.pack()
        self.ala_kehys.pack()

        tkinter.mainloop()

    def nayta_valinta(self):
        selections = []
        if self.var1.get() == 1:
            selections.append("Vaihtoehto 1")
        if self.var2.get() == 1:
            selections.append("Vaihtoehto 2")
        if self.var3.get() == 1:
            selections.append("Vaihtoehto 3")

        if selections:
            tkinter.messagebox.showinfo('Valinta', 'Sinä valitsit: ' + ', '.join(selections))
        else:
            tkinter.messagebox.showinfo('Valinta', 'Et valinnut mitään.')


oma_gui = OmaGUI()
