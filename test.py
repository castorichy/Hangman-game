
import random as r
import time

r.seed()
letters = ""

for i in range(6):
    letters += r.choice("qwertyuioplkjhgfdsazxcvbnm")

data = []
with open("words.txt", "r") as f:
    data = f.read().split("\n")


print(letters)
