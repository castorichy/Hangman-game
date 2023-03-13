w_l = ["hello", "sweet", "sweetest"]

def word_box_display(word = ""):
    """ Counts the words and print them in a box"""
    rang = len(word)
    for ch in word:
        print("\t - ", end="")
        print(f"\t|{ch}|", end="")
        print("\t - ", end="")
    print()
for w in w_l:
    word_box_display(w)

