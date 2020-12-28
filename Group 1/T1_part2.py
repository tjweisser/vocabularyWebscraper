# Part 2

# 1. How sentimental?
import csv
import pandas as pd
import numpy as np

# ask user for input
entered_word = input("Enter a word to look up ")

# load csv
data = pd.read_csv(r"sentiment.csv")
df = pd.DataFrame(data)
df.columns = ["word", "sentiment"]

# try to find word
try:
    print(df.loc[df["word"] == entered_word.lower(), "sentiment"].iloc[0])
except:
    print("Word not in file")

# 2.
# ask user for sentence
ent_sentence = input("Enter a sentence to scrape ")

# split sentence
word_list = ent_sentence.split()
print(word_list)

sum_list = 0
for word in word_list:
    try:
        item = df.loc[df["word"] == word, "sentiment"].iloc[0]
        sum_list += item
    except:
        sum_list += 0

if sum_list < 0:
    print("Negative sentiment detected")
elif sum_list == 0:
    print("None of the words were found")
else:
    print("Positive sentiment detected")
