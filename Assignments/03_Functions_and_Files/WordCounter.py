"""
Q1: Word Counter

Ask the user for a file name. 
Count and display the number of words in the file. 
Also, identify the most frequent word and how many times it appears.
"""

# I will use dictionary to store the word and it is appearance frequency

import os

fileName = input("Please enter a full file name(e.g., data.txt): ")

if os.path.exists(fileName):
    with open(fileName, "r") as f:
        content = f.read()

        words = content.split()
        word_count = len(words)
        print("Total number of words:", word_count)
        
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
                
        most_frequent_word = max(word_freq, key=word_freq.get)
        print("Most frequent word:", most_frequent_word)
        print("It appears", word_freq[most_frequent_word], "times.")

else:
    print("File does not exist.")
