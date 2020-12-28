# Part 3

####### 1.
import requests as req
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np


# load sentiment data
data = pd.read_csv(r"sentiment.csv")
df = pd.DataFrame(data)
df.columns = ["word", "sentiment"]

# load reviews
response = req.get(
    """https://www.tripadvisor.com/Restaurant_Review-g187147-d1751525-Reviews-Cafe_Le_Dome-Paris_Ile_de_France.html"""
)

# is code == 200?
if response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, "lxml")

else:
    print("Failed to get a response from the url. Error code:", response.status_code)


# Extract the sentiment
count = 1
for review in soup.find_all("p", class_="partial_entry"):
    print(f"Review {count}")

    count += 1
    ent_sentence = review.text
    # split sentence
    word_list = ent_sentence.split()

    sum_list = 0
    for word in word_list:
        try:
            item = df.loc[df["word"] == word.lower(), "sentiment"].iloc[0]
            sum_list += item
        except:
            sum_list += 0

    if sum_list < 0:
        print(f"Negative sentiment detected. Sentiment score: {sum_list}")
    elif sum_list == 0:
        print("None of the words were found")
    else:
        print(f"Positive sentiment detected. Sentiment score: {sum_list}")
    print("------------------------------------------------------------")

# 2. Get the user rated review

# load reviews
response = req.get(
    """https://www.tripadvisor.com/Restaurant_Review-g187147-d1751525-Reviews-Cafe_Le_Dome-Paris_Ile_de_France.html"""
)

# is code == 200?
if response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, "lxml")

else:
    print("Failed to get a response from the url. Error code:", response.status_code)

# The following code is unfinished since we ran out of time :(
# Extract the stars rating
count = 1
for stars in soup.find_all("span", class_="ui_bubble_rating bubble_40"):
    print(f"Review {count}")
    print(item.get_text(strip=True))
    count += 1
