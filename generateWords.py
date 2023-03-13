import time
import random as r
class GenerateWords:
    """ Generates sorted worsds to be used in hangman game """

    def __read_file(self, line_no: int):
        """ Reads the file and return a word in a given line """
        data = []
        with open("words.txt", "r") as f:
            data = f.read().split("\n")
        return data[line_no]

    def __random_select_line(self):
        """ Randomly selects lines to extracted form the file """
        words = []
        r.seed()
        for i in range(0, 6):
            line = r.randint(1, 1001)
            rd = self.__read_file(line)
            words.append(rd)
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
        return words

    def get_word_list(self):
        return self.__sort_by_length()


class HangmanControler:
    """ Controls all algorithm and validates game artributes """
    def __init__(self) -> None:
        super().__init__()


class PlayHangman(GenerateWords, HangmanControler):
    """ it is the main presentation controler. in give output and input """

    def __init__(self) -> None:
        super().__init__()
        self.word_list = self.get_word_list()

    def word_in_box(self):
        """ Counts the words and print them in a box"""
        for word in self.word_list:
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




if __name__ == "__main__":
    pl = PlayHangman()
    pl.word_in_box()

