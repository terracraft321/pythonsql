import tkinter


class OMAGUI:
    def __init__(self):
        # luodaan ikkunakomponentti
        self.paa_ikkuna = tkinter.Tk()

        # tässä voit lisätä muita komponentteja ja toiminnallisuutta

        # pääsilmukka
        self.paa_ikkuna.mainloop()


def main():
    oma_gui = OMAGUI()


if __name__ == "__main__":
    main()
