#!/usr/local/bin/python3
import requests as req
from bs4 import BeautifulSoup
import sys
import pyperclip as pc

sys.argv

# get user query
if len(sys.argv) > 1:
    word = ''.join(sys.argv[1:])
else:
    word = pc.paste()

# get HTML for definition, word family, and language level
res = req.get('https://dictionary.cambridge.org/dictionary/english/' + word)
soup = BeautifulSoup(res.text, 'lxml')

# get HTML for synonyms
res2 = req.get('https://www.merriam-webster.com/thesaurus/' + word)
soup2 = BeautifulSoup(res2.text, 'lxml')

# extract definition, family, examples, synonyms, language level, and audio
try:
    # definition
    definition = str.strip(soup.find('div', class_='def ddef_d db').text)
    # word type
    family = [str.strip(div.text) for div in
              soup.findAll('div', class_='posgram dpos-g hdib lmr-5')]
    # some example sentences
    examples = [str.strip(div.text) for div in
                soup.findAll('div', class_='examp dexamp')]
    # some synoyms
    synonyms = [str.strip(div.text) for div in
                soup2.findAll('div', class_='thes-list-content synonyms_list')]

    # print type and definition
    print(f'type: {family[0]}\n'
          f'definition: {definition[:-1]}')
    # handle synoyms
    if len(synonyms) < 1:
        print("synoyms: The word you've entered isn't"
              "in the Merriam Webster thesaurus")
    else:
        print(f'synoyms: {synonyms[0]}')
    # print some examples, but fewer than four
    count = 1
    for i in examples:
        if count < 4:
            print('example ' + str(count) + ") " + i)
            count += 1

# handle exception
except Exception as e:
    print(e)
