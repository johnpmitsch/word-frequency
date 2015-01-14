import re
import sys


def word_frequency(input_file):
    """Takes a text file as an input and prints a list of the 20 most
       common words in the file. Capitalization and punctuation are negated"""
    scrubbed_words = []
    word_dict = {}
    x = 0

    # Open file and split on each new line
    file = open(input_file)
    lines = file.read().split("\n")

    # Normalize text by removing punctuation and capitalization
    # then store in the list scrubbed_words
    for line in lines:
        unscrubbed_words = line.split(" ")
        for word in unscrubbed_words:
            scrubbed_word = re.sub(r'[^A-Za-z]', "", word).lower()
            if scrubbed_word != '':
                scrubbed_words.append(scrubbed_word)

    # Iterate through list of words
    for word in scrubbed_words:
        # Store words in dictionary with amount of occurences as value
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    # Sort dictionary by amount of occurences and store in list
    # of tuples. The 0 index of each tuple is the word and the
    # 1 index is the amount of occurences
    word_dict_sorted = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    histogram_amount = word_dict_sorted[0][1]
    print(" ")

    # Print out top 20 most common occurences and a
    # corresponding histogram made of # characters.
    # The highest value is 50 and the rest of the values
    # are scaled in proportion
    while x < 20:
        hash_marks = int(round(word_dict_sorted[x][1] * 50 / histogram_amount, 0))
        print("{0:10}".format(word_dict_sorted[x][0]), '#' * hash_marks)
        x += 1

    file.close()

word_frequency(sys.argv[1])
