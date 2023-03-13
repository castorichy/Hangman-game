import os
import time
import random as r
from extractWords import Test

class GenerateWords(Test):
    """ Generates sorted worsds to be used in hangman game """

    __word_list = []
    __sorted_word_list = []
    choice_word = ""

    def __init__(self) -> None:
        super().__init__()
        self.set_got_word_list()
        self.__word_list = GenerateWords.__word_list
        self.__word_list = self.get_got_word_list()
        #self.choice_word = GenerateWords.__choice_word
        #self.choice_word = self.choice_word_shuffal()

    def __random_select_line(self):
        """ Randomly selects lines to extracted from the file """
        words = []
        r.seed()
        for i in range(0, 6):
            wor = r.choice(self.__word_list)
            words.append(wor)
        return words

    def __sort_by_length(self)-> list:
        """ Sorts the extracted words by length using bubble sort algorithm and returns sor        ted list """
        words = self.__random_select_line()

        for iter_num in range(len(words)-1,0,-1):
            for idx in range(iter_num):
                if len(words[idx])>len(words[idx+1]):
                    temp = words[idx]
                    words[idx] = words[idx+1]
                    words[idx+1] = temp
        words = list(set(words))
        if len(words) < 3:
            self.__init__()
        else:
            return words

    def set_word_list(self):
        self.__sorted_word_list = self.__sort_by_length()

    def get_word_list(self):
        return self.__sorted_word_list
    def set_choice_word(self):
        self.choice_word = self.choice_word_shuffal()


class HangmanControler(GenerateWords):
    """ Controls all algorithm and validates game artributes """
    def __init__(self) -> None:
        super().__init__()
        self.word_list = self.get_word_list()

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
        self.set_choice_word()
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
        self.set_choice_word()
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

    def word_box_display(self):
        """ Counts the words and print them in a box"""
        for word in self.__word_list:
            rang = len(word)
            for i in range(rang):
                print("\t --- ", end=" ")
            print()

            for i in range(rang):
                print(f"\t| {word[i]} |", end=" ")
            print()

            for i in range(rang):
                print("\t --- ", end=" ")
            print()






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
        print("LATTERS THAT FORM A WORD FROM TABLE BELLOW Press")
        self.set_choice_word()
        self.display_shuffle()
        choice = input("""\
* (Q/q) Quit
* (enter without Space) shuffle words
* (r/R) to reset game
    You Guess: """).lower()

        match choice:
            case "q":
                exit()
            case "":
                self.set_choice_word()
                self.display_shuffle()
                self.user_choice()
            case "r":
                pass
            case other:
                self.validate_user_choice(choice)


    def validate_user_choice(self, choice):
        pass


tl = PlayHangman()
tl.display_shuffle()
tl.user_choice()

