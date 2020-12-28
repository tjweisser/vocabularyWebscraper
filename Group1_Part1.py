# Part 1

# 1. Hello there
# first_name = input("Enter your first name: ")
# print(f"Hello {first_name}, have a nice hands-on session!")

# 2. Management talk
# a.
from random import randint

# b.
part_1 = [
    "We will constantly strive",
    "We will continue",
    "We are dedicated",
    "We will help",
    "We are continually evolving",
    "We will steadfastly and unceasingly try",
    "We will progressively conceptualize",
    "We will uniquely orchestrate",
]
part_2 = [
    "to provide",
    "to helping enable",
    "to leverage",
    "to deliver",
    "to control",
    "to research",
    "to imbibe",
]
part_3 = [
    "flexible knowledge products",
    "worldwide ePortals",
    "digital database solutions",
    "data‐driven business metrics",
    "scalable solutions",
    "virtual eSolutions",
    "short term solutions with long term vision",
    "world class frameworks",
]
part_4 = [
    "for today's",
    "for tomorrow’s",
    "for increasing the market potential of",
    "for innovative",
    "for budding",
]
part_5 = [
    "market‐focused virtual eMonopolies.",
    "Fortune 500 dot‐com virtual corporations.",
    "Brazilian market leaders.",
    "virtual businesses.",
    "Scandinavian information workers.",
    "new economy eCompanies.",
    "industry champions.",
    "business gurus.",
    "secrets of the universe.",
]


# c.
def randomSentences(number_of_sen):
    for j in range(0, number_of_sen):
        sent = []
        for i in (part_1, part_2, part_3, part_4, part_5):
            sen = i[randint(0, len(i) - 1)]
            sent.append(sen)
        print(" ".join(sent))


# randomSentences(2)

# user_choice_num_sen = input("How many random sentences would you like to print? ")
# randomSentences(int(user_choice_num_sen))

# Part 2

# 1. How sentimental?
import csv
import pandas as pd
import numpy as np

sentiment_csv = "sentiment.csv"
entered_word = input("Enter a word to look up ")


data = pd.read_csv(r"sentiment.csv")
df = pd.DataFrame(data)
df.columns = ["word", "sentiment"]

# try to find word
try:
    print(df.loc[df["word"] == entered_word, "sentiment"].iloc[0])
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

print(sum_list)
