
class Hangman:

    words = ["Hello", "Worlds", "Jame", "Kim"]

    def word_in_box(self, word: str):
        """ Counts the words and print them in a box"""
        try:
            rang = len(word)
            for i in range(rang):
                print(" --- ", end=" ")
            print()

            for i in range(rang):
                print(f"| {word[i]} |", end=" ")
            print()

            for i in range(rang):
                print(" --- ", end=" ")
            print()
        except ValueError:
            return -1

    def word_chooser(self):
        pass

hang = Hangman()
hang.word_chooser()
