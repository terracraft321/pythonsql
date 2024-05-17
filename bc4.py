import tkinter

class OmaGUI:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()
        self.teksti = tkinter.Label(self.paa_ikkuna, text="Hei Maailma")
        self.teksti2 = tkinter.Label(self.paa_ikkuna, text="Oma graafinen näyttöliittymä")
        self.teksti.pack(side='left')
        self.teksti2.pack(side='left')
        self.paa_ikkuna.mainloop()

def main():
    oma_gui = OmaGUI()

if __name__ == "__main__":
    main()
