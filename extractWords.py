
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
    words = []
    six_words = []

    def __main_word(self):
        """ Generates main word to be used in searching hangman words """

        with open("words.txt", "r") as f:
            self.data = f.read().split("\n")

        for word in self.data:
            if len(word) >= 4 and len(word) <= 6:
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

    def __six_word_celector(self):
        self.__word_finder()
        r.seed()
        six_words = []
        if len(self.got_word_list) < 4:
            self.got_word_list.clear()
            self.__word_finder()
        else:
            for i in range(len(self.got_word_list)):
                if len(six_words) == 6:
                    break
                while True:
                    six_word = r.choice(self.got_word_list)
                    if six_word not in six_words:
                        six_words.append(six_word)
                        break
                    else:
                        continue
        self.got_word_list = six_words
        if self.word_main not in self.got_word_list:
            r.seed()
            l = r.randint(2, 4)
            self.got_word_list.remove(self.got_word_list[l])
            self.got_word_list.insert(l - 1, self.word_main)

    def __sort_by_length(self):
        """ Sorts the extracted words by length using bubble sort algorithm and returns sor        ted list """
        self.__six_word_celector()
        words = self.got_word_list

        for iter_num in range(len(words)-1,0,-1):
            for idx in range(iter_num):
                if len(words[idx])>len(words[idx+1]):
                    temp = words[idx]
                    words[idx] = words[idx+1]
                    words[idx+1] = temp
        words = list(set(words))

        if len(words) < 3:
            self.__word_finder()
        else:
            self.words = words


    def choice_word_shuffal(self):
        """ Randomly Reshufles main_word atribute """
        word = self.word_main
        r.seed()
        shaffle_word = []
        for ch in word:
            shaffle_word.append(ch)
        r.shuffle(shaffle_word)

        shuffled_word = "".join(shaffle_word)
        return shuffled_word

    def set_got_word_list(self):
        """ sets got_word_list artribute
        Run this function before running get_got_word_list"""
        self.__main_word()
        self.__word_finder()
        self.__six_word_celector()
        self.__sort_by_length()

    def get_got_word_list(self):
        """ returns got_word_list artribute
        Run this function before running get_got_word_list"""
        return self.got_word_list


if __name__ == "__main__":
    Test()
