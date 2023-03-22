import os
import time
import random as r
from extractWords import Test
from ReadJson import ReadJson

class GenerateWords(Test, ReadJson):
    """ Generates sorted worsds to be used in hangman game """

    __word_list = []
    __sorted_word_list = []
    choice_word = ""

    def __init__(self) -> None:
        super().__init__()
        self.set_got_word_list()
        self.word_list = GenerateWords.__word_list
        self.word_list = self.get_got_word_list() # Generated words
        self.choice_word = self.get_word_list()

        '''def __random_select_line(self):
        """ Randomly selects lines to extracted from the file """
        words = []
        r.seed()
        for i in range(0, 6):
            wor = r.choice(self.__word_list)
            words.append(wor)
        return words'''


    def set_word_list(self):
        self.set_got_word_list()
        #self.__sorted_word_list = self.__sort_by_length()
        #print(self.__sorted_word_list)

    def get_word_list(self):
        return self.__sorted_word_list

    def set_choice_word(self):
        self.choice_word = self.choice_word_shuffal()

    def get_choice_word(self):
        return self.choice_word


class HangmanControler(GenerateWords):
    """ Controls all algorithm and validates game artributes """
    def __init__(self) -> None:
        super().__init__()
        #self.set_got_word_list()
        #self.word_list = self.get_got_word_list()
        #print(self.word_list)

    def choices_display_6(self):
        """ this is reshuffling precentetion """
        ch = self.choice_word
        print("\t\t   -  \t   - ")
        print(f"\t\t  |{ch[0]}| \t  |{ch[1]}|")
        print("\t\t   -  \t   - ")

        print("\t    -  \t\t\t  - ")
        print(f"\t   |{ch[2]}| \t\t\t |{ch[3]}|")
        print("\t    -  \t\t\t  - ")

        print("\t\t   -  \t   - ")
        print(f"\t\t  |{ch[4]}| \t  |{ch[5]}|")
        print("\t\t   -  \t   - ")

    def choices_display_5(self):
        """ this is reshuffling precentetion """
        #self.set_choice_word()
        ch = self.choice_word
        print("\t\t   - ")
        print(f"\t\t  |{ch[0]}| ")
        print("\t\t   - ")

        print("\t    -  \t\t\t  - ")
        print(f"\t   |{ch[1]}| \t\t\t |{ch[2]}|")
        print("\t    -  \t\t\t  - ")

        print("\t\t   -  \t   - ")
        print(f"\t\t  |{ch[3]}| \t  |{ch[4]}|")
        print("\t\t   -  \t   - ")

    def choices_display_4(self):
        """ this is reshuffling precentetion """
       # self.set_choice_word()
        ch = self.choice_word
        print("\t\t   -  \t   - ")
        print(f"\t\t  |{ch[0]}| \t  |{ch[1]}|")
        print("\t\t   -  \t   - ")

        print("\t\t   -  \t   - ")
        print(f"\t\t  |{ch[2]}| \t  |{ch[3]}|")
        print("\t\t   -  \t   - ")

    def shuffle_msg_display(self):
        print("""\
        \tCHOOSE LATTERS THAT FORM A WORD FROM TABLE BELLOW
         Press
         * (Q/q) Quit
         * (enter) shuffle words
         * (r/R) to reset game

              """)
    def dispay_correct_word_2(self, cor_word = ""):
        if len(cor_word) == 0:
            print("\t  ---   --- ")
            print(f"\t |   | |   |")
            print("\t  ---   ---")
        else:
            print("\t ---   --- ")
            print(f"\t| {cor_word[0]} | | {cor_word[1]} |")
            print("\t ---   ---")
    def dispay_correct_word_3(self, cor_word = ""):
        if len(cor_word) == 0:
            print("\t  ---   ---   --- ")
            print(f"\t |   | |   | |   |")
            print("\t  ---   ---   ---")
        else:
            print("\t ---   ---   --- ")
            print(f"\t| {cor_word[0]} | | {cor_word[1]} | | {cor_word[2]} |")
            print("\t ---   ---   ---")

    def dispay_correct_word_4(self, cor_word = ""):
        if len(cor_word) == 0:
            print("\t  ---   ---   ---   ---")
            print(f"\t |   | |   | |   | |   |")
            print("\t  ---   ---   ---   ---")
        else:
            print("\t ---   ---   ---   ---  ")
            print(f"\t| {cor_word[0]} | | {cor_word[1]} | | {cor_word[2]} | | {cor_word[3]} |")
            print("\t ---   ---   ---   ---")

    def dispay_correct_word_5(self, cor_word = ""):
        if len(cor_word) == 0:
            print("\t  ---   ---   ---   ---   ---")
            print(f"\t |   | |   | |   | |   | |   |")
            print("\t  ---   ---   ---   ---   ---")
        else:
            print("\t ---   ---   ---   ---   ---  ")
            print(f"\t| {cor_word[0]} | | {cor_word[1]} | | {cor_word[2]} | | {cor_word[3]} | | {cor_word[4]} |")
            print("\t ---   ---   ---   ---   ---")
    def dispay_correct_word_6(self, cor_word = ""):
        if len(cor_word) == 0:
            print("\t  ---   ---   ---   ---   ---   ---")
            print(f"\t |   | |   | |   | |   | |   | |   |")
            print("\t  ---   ---   ---   ---   ---   ---")
        else:
            print("\t ---   ---   ---   ---   ---   ---  ")
            print(f"\t| {cor_word[0]} | | {cor_word[1]} | | {cor_word[2]} | | {cor_word[3]} | | {cor_word[4]} | | {cor_word[5]} |")
            print("\t ---   ---   ---   ---   ---   ---")


    def validate_empty_value(self, idx):

        match len(self.word_list[int(idx) - 1]):
            case 2:
                self.dispay_correct_word_2("")
            case 3:
                self.dispay_correct_word_3("")
            case 4:
                self.dispay_correct_word_4("")
            case 5:
                self.dispay_correct_word_5("")
            case 6:
                self.dispay_correct_word_6("")

    def Display_homePage(self):
        for i in range(1, 7):
            val = self.readJson(i)
            idx = val[0]
            value = val[1]
            match len(val[1]):
                case 0:
                    self.validate_empty_value(idx)
                case 2:
                    self.dispay_correct_word_2(val[1])
                case 3:
                    self.dispay_correct_word_3(val[1])
                case 4:
                    self.dispay_correct_word_4(val[1])
                case 5:
                    self.dispay_correct_word_5(val[1])
                case 6:
                    self.dispay_correct_word_6(val[1])

class PlayHangman(HangmanControler):
    """ it is the main presentation controler. in give output and input """

    def __init__(self) -> None:
        super().__init__()

    def display_shuffle(self):
        if len(self.choice_word) == 4:
            self.choices_display_4()
        elif len(self.choice_word) == 5:
            self.choices_display_5()
        elif len(self.choice_word) == 6:
            self.choices_display_6()
        else:
            print("Display Not Available")

    def user_choice(self):
        os.system("clear")
        self.Display_homePage()
        print("LATTERS THAT FORM A WORD FROM TABLE BELLOW Press")
        self.set_choice_word()
        self.display_shuffle()
        print(self.word_list)
        while True:
            choice = input("""\
    * (Q/q) Quit
    * (enter without Space) shuffle words
    * (r/R) to res
    t game
        You Guess: """).lower()

            match choice:
                case "q":
                    exit()
                case "":
                    self.Display_homePage()
                    self.set_choice_word()
                    self.display_shuffle()
                    self.user_choice()
                case "r":
                    self.resetJson()
                    self.user_choice()
                case other:
                    if self.validate_user_choice(choice) != 1:
                        self.user_choice()
                    else:
                        break


    def validate_user_choice(self, choice):
        if choice in self.word_list:
            self.check_index(choice)
        else:
            return -1

    def check_index(self, word):
        for idx, elem in enumerate(self.word_list):
            if word == elem:
                self.writeJson({f"{idx + 1}": word})


tl = PlayHangman()
tl.user_choice()
print(tl.word_list)
