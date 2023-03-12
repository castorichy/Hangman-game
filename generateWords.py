import time
import random as r

class GenerateWords:
    sorted_words= []

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

    def __sort_by_length(self):
        """ Sorts the extracted words by length using bubble sort algorithm and returns sor        ted list """
        list = self.__random_select_line()
        for iter_num in range(len(list)-1,0,-1):
          for idx in range(iter_num):
             if len(list[idx])>len(list[idx+1]):
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
        return list

    def get_word_list(self):
        return self.__sort_by_length()

if __name__ == "__main__":
    GenerateWords()

