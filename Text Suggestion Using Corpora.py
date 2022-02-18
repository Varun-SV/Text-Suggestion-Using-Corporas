# -*- coding: utf-8 -*-
"""

###Importing Libraries
"""

from nltk.util import ngrams
from nltk.tokenize import word_tokenize as wt
import nltk
nltk.download('punkt')

"""###Functions """

#@title Function for Creation of Complex punctuation 
def listenhancer(lst,lists):
  # lst = ['a','b']
  # lists = ['c','d']
  res=[]
  # res.append(lst)
  # res.append(lists)
  for i in lst:
    res.append(i)
    for j in lists:
      res.append(j)
  for i in lst:
    for j in lists:
      res.append(i+j)
  return res

#@title Punctuations
from string import punctuation
puns = list(punctuation)
print(puns)
print(len(puns))
pun=[]
pun = listenhancer(puns,puns)
print(pun)
print(len(pun))

from nltk.tokenize import word_tokenize as wt 
def cleaning(Datas):
  lower = []
  tokens = []
  cleaned_tokens=[]
  tokens = wt(Datas)
  for i in tokens:
    lower.append(i.lower())
  cleaned_tokens = [token for token in lower if token not in pun]
  new_data = ''
  for i in cleaned_tokens:
    new_data+=i
    new_data+=' '
  return new_data

def extract_ngrams(data,num):
  n_grams = ngrams(nltk.word_tokenize(data),num)
  return [' '.join(grams) for grams in n_grams]



data = open("/content/tomsawyer_corpora.txt","r",encoding='utf8').read()
data.lower()

cleaned_data=cleaning(data)

monograms = extract_ngrams(data,1)
len(monograms)


print("The totla number of Tokens in the document = "+str(len(monograms)))

"""####Result:
---
From this ans we can get the information about the number of total tokens present in the corpus and can then use this information for the proving of Zipf's law as well as prediction of a word from the given word.

###Answer 2.b
"""

fdd = nltk.FreqDist(monograms)

fdd.tabulate()

#@title ANS b
print("The Frequency Distribution of each words : \n")
str(fdd.pprint())

"""####Result:
---
From this ans we can get the frequency distribution for each words separately, which later can be used to prove the Zipf's Law.


"""

import re
from operator import itemgetter    
freq = {}
frequency = {}
words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', data)
 
for word in words:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
for key, value in reversed(sorted(frequency.items(), key = itemgetter(1))):
  freq[key]=value

from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

freqs = []
wrds=[]
ranks=[]
rank = {}
rank_no = 1
for i in take(10,freq):
  rank[rank_no] = i
  wrds.append(i)
  ranks.append(rank_no)
  rank_no+=1
  freqs.append(freq[i])
  print(i+" : "+str(freq[i]))

print(freqs)

print(ranks)

import matplotlib.pyplot as plt
plt.subplots_adjust(left=2,
                    bottom=0.1, 
                    right=4, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)


plt.xlabel("Word")
plt.ylabel("Frequency")
plt.subplot(1,2,1)
plt.plot(wrds,freqs,label="Zipf's Law",color="green")
plt.legend()
plt.xlabel("Word/Rank")
plt.ylabel("Frequency")
plt.subplot(1,2,2)
plt.plot(ranks,freqs,label="Zipf's Law",color="red")
plt.legend()
plt.show()

"""####*Result* : 
---
  From the above graphs we can get a relation of **f** being ***inversely proportional to r*** where ***f*** represents ***Frequency*** and ***r*** represents ***Rank***.

"""

def correct_misspelled(misspelled):
  suggestions = []
  for i in words:
    if ((misspelled in i) or (i in misspelled)):
      if abs(len(misspelled or i) - len(misspelled and i)) <=3:
        if (i or misspelled) not in suggestions:
          suggestions.append(i or misspelled)
  return suggestions

def sort_by_rank(suggestion):
  new_suggestions=[]
  for i in range(len(suggestion)):
    maxs = freq[suggestion[i]]
    maxstr = suggestion[i]
    for j in range(i,len(suggestion)):
      if maxs < freq[suggestion[j]]:
        maxs = freq[suggestion[j]]
        maxstr = suggestion[j]
    new_suggestions.append(maxstr)
    return new_suggestions


string = input("Enter a word : ")
print("Suggestions : \n")
print(correct_misspelled(string))

print("Suggestion Based on Rank : ")
print(sort_by_rank(correct_misspelled(string)))

"""####Result: 
---
From this one we are able to get all the words containing the searched word and will suggest the word which is closest to the misspelled words.
"""
