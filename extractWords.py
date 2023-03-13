
import time
import random as r

class Test:

    r.seed()

    word_len = r.randint(4, 6)

    data = []
    search_word = []
    got_word_list = []


    main_data = []
    word_main = ""

    def __main_word(self):
        """ Generates main word to be used in searching hangman words """

        with open("words.txt", "r") as f:
            self.data = f.read().split("\n")

        for word in self.data:
            if len(word) == 6:
               self.search_word.append(word)

        self.word_main = r.choice(self.search_word)

    def __word_finder(self):
        """ finds words to be used """
        self.__main_word()
        got_word = ""
        #finds words with the same latters with main_word artribute
        for word in self.data:
            for w in word:
                if w in self.word_main:
                    got_word += w
                else:
                    got_word = ""

            if len(got_word) >= 2:
                if got_word in self.data:
                    self.got_word_list.append(got_word)
                    got_word = ""
                else:
                    got_word = ""
            else:
                got_word = ""
        #remove Duplicate in the got_word_list
        self.got_word_list = list(set(self.got_word_list))

    def set_got_word_list(self):
        """ sets got_word_list artribute
        Run this function before running get_got_word_list"""
        self.__word_finder()

    def get_got_word_list(self):
        """ returns got_word_list artribute
        Run this function before running get_got_word_list"""

        return self.got_word_list


if __name__ == "__main__":
    Test()
