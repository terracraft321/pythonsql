import tkinter
import tkinter.messagebox

class OmaGUI:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()
        self.oma_painike = tkinter.Button(self.paa_ikkuna, text = "Paina minua ;)", command = self.tee_jotain)
        self.oma_painike.pack()
        tkinter.mainloop()

    def tee_jotain(self):
        tkinter.messagebox.showinfo('Vastaus', 'Kiitos klikkaukesta beibi')

oma_gui = OmaGUI()