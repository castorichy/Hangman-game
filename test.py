
words = ["Hello", "Lol", "kella"]


join_word = "".join(words).lower()

ch_list = []

for ch in join_word:
    ch_list.append(ch)

print(set(ch_list))

