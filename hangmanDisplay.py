class HangManDisplay:

    def __init__(self) -> None:
        pass

    def choices_display_6(self, ch):
        """ this is reshuffling precentetion """
        print("\t\t\t   -  \t   - ")
        print(f"\t\t\t  |{ch[0]}| \t  |{ch[1]}|")
        print("\t\t\t   -  \t   - ")

        print("\t\t    -  \t\t\t  - ")
        print(f"\t\t   |{ch[2]}| \t\t\t |{ch[3]}|")
        print("\t\t    -  \t\t\t  - ")

        print("\t\t\t   -  \t   - ")
        print(f"\t\t\t  |{ch[4]}| \t  |{ch[5]}|")
        print("\t\t\t   -  \t   - ")

    def choices_display_5(self, ch):
        """ this is reshuffling precentetion """
        print("\t\t\t\t - ")
        print(f"\t\t\t\t|{ch[0]}| ")
        print("\t\t\t\t - ")

        print("\t\t    -  \t\t\t  - ")
        print(f"\t\t   |{ch[1]}| \t\t\t |{ch[2]}|")
        print("\t\t    -  \t\t\t  - ")

        print("\t\t\t   -  \t   - ")
        print(f"\t\t\t  |{ch[3]}| \t  |{ch[4]}|")
        print("\t\t\t   -  \t   - ")

    def choices_display_4(self, ch):
        """ this is reshuffling precentetion """
        print("\t\t\t   -  \t   - ")
        print(f"\t\t\t  |{ch[0]}| \t  |{ch[1]}|")
        print("\t\t\t   -  \t   - ")

        print("\t\t\t   -  \t   - ")
        print(f"\t\t\t  |{ch[2]}| \t  |{ch[3]}|")
        print("\t\t\t   -  \t   - ")

if __name__ == "__main__":
    t = HangManDisplay()
    t.choices_display_5("Hello")
    t.choices_display_4("Hell")
    t.choices_display_6("Hellon")
