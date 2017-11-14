import nltk
import re

target = open('word_to_index_100.txt', 'w')
file = nltk.data.path[0] + '/corpora/brown/brown_vocab_100.txt'
words = dict()
with open(file) as f:
	for index, line in enumerate(f):
		words[line.rstrip()] = index
target.write(str(words))
target.close()
