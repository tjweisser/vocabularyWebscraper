import requests as req
from bs4 import BeautifulSoup

# get HTML for definition, word family, and language level
response = req.get(
    """https://www.tripadvisor.com/Restaurant_Review-g227613-d3531819-Reviews-Le_Jardin_Napolitain-
Jouy_en_Josas_Versailles_Yvelines_Ile_de_France.html"""
)

# is code == 200?
if response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, "lxml")

else:
    print("Failed to get a response from the url. Error code:", response.status_code)


# definition
# definition = str.strip(soup.find("p", class_="partial_entry").text)
count = 1
for review in soup.find_all("p", class_="partial_entry"):
    print(f"Review {count}")
    print(review.text)
    print("------------------------------------------------------------")
    count += 1

# print type and definition
# print(f"Review: {definition}")
