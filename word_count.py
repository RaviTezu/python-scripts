#!/usr/bin/python

from __future__ import print_function
import sys

def count_words(f_name):
    """ Take a filename as argument and returns a dictionary
        of words in the files as keys and their count as values """
    word_count = {}
    try:
	with open(sys.argv[1], 'r') as f: 
            for line in f: 
                for word in line.split():
                    word_count[word] = word_count.get(word, 0) + 1
        return word_count
    except IOError as e:
       print("USAGE: " + sys.argv[0] + " <file_name>")
       print(e)
       sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        wc_dict = count_words(sys.argv[1])
        print(wc_dict)
    else: 
        print("USAGE: " + sys.argv[0] + " <file_name>")
        sys.exit(1)
