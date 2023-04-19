# This is an anagram maker that takes an English word as an input and prints out its anagrams.

import urllib.request
from itertools import permutations

# Download the word list and save it to a file
url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
filename = 'words_alpha.txt'
urllib.request.urlretrieve(url, filename)

# Read the EOWL list into a set
with open(filename, 'r') as f:
    word_list = set(word.strip().lower() for word in f)

# Get user input word
word = input("Enter a word: ")

# Generate anagrams of the input word
perms = [''.join(p) for p in permutations(word)]
anagrams = [perm for perm in perms if perm in word_list and perm != word]

# Print the anagrams
if anagrams:
    print(f"Anagrams of '{word}':")
    for anagram in anagrams:
        print(anagram)
else:
    print(f"No anagrams of '{word}' found.")