
from squareShape import Test

t = Test()

main_word = t.main_word()
words = t.data
found_word = ''

for i in range(1000):
    for ch in words[i]:
        if ch in main_word:
            found_word += ch
        else:

            found_word = ""
    if len(found_word) >= 3:
        if found_word in words:
            print(found_word)
            found_word = ""
        else:
            found_word = ""
    else:
        found_word = ""


print("word: ", main_word)
print(found_word)


