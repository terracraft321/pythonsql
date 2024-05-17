import tkinter

class OmaGUI:
    def __init__(self):
        self.paa_ikkuna = tkinter.Tk()

        self.teksti = tkinter.Label(self.paa_ikkuna, text='Hei Maailma')

        self.teksti.pack()

        tkinter.mainloop()

def main():
    oma_gui = OmaGUI()

if __name__ == "__main__":
    main()
